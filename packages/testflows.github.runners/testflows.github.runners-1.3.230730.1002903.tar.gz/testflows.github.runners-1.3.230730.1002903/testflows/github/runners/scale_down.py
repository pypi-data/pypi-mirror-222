# Copyright 2023 Katteli Inc.
# TestFlows.com Open-Source Software Testing Framework (http://testflows.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time
import copy
import logging
import threading

from dataclasses import dataclass

from .actions import Action
from .scale_up import (
    server_name_prefix,
    runner_name_prefix,
    standby_runner_name_prefix,
    StandbyRunner,
)
from .logger import logger

from github.Repository import Repository
from github.SelfHostedActionsRunner import SelfHostedActionsRunner

from hcloud import Client
from hcloud.servers.client import BoundServer


@dataclass
class PoweredOffServer:
    """Powered off server."""

    time: float
    server: BoundServer
    observed_interval: float


@dataclass
class ZombieServer:
    """Zombie server."""

    time: float
    server: BoundServer
    observed_interval: float


@dataclass
class UnusedRunner:
    """Unused self-hosted runner."""

    time: float
    runner: SelfHostedActionsRunner
    observed_interval: float


def scale_down(
    terminate: threading.Event,
    repo: Repository,
    client: Client,
    max_powered_off_time: int,
    max_unused_runner_time: int,
    max_runner_registration_time: int,
    interval: int,
    debug: bool = False,
    standby_runners: list[StandbyRunner] = None,
):
    """Scale down service by deleting any powered off server,
    any server that has unused runner, or any server that failed to register its
    runner (zombie server).
    """
    powered_off_servers: dict[str, PoweredOffServer] = {}
    unused_runners: dict[str, UnusedRunner] = {}
    zombie_servers: dict[str, ZombieServer] = {}

    while True:
        current_interval = time.time()

        if terminate.is_set():
            with Action("Terminating scale down service"):
                break

        try:
            with Action("Getting list of servers", level=logging.DEBUG):
                servers: list[BoundServer] = client.servers.get_all()
                servers = [
                    server
                    for server in servers
                    if server.name.startswith(server_name_prefix)
                ]

            with Action("Getting list of self-hosted runners", level=logging.DEBUG):
                runners: list[SelfHostedActionsRunner] = repo.get_self_hosted_runners()

            with Action(
                "Looking for powered off or zombie servers", level=logging.DEBUG
            ):
                for server in servers:
                    if server.status == server.STATUS_OFF:
                        if server.name not in powered_off_servers:
                            with Action(f"Found new powered off server {server.name}"):
                                powered_off_servers[server.name] = PoweredOffServer(
                                    time=time.time(),
                                    server=server,
                                    observed_interval=current_interval,
                                )
                        powered_off_servers[server.name].server = server
                        powered_off_servers[
                            server.name
                        ].observed_interval = current_interval

                    elif server.status == server.STATUS_RUNNING:
                        if server.name not in [runner.name for runner in runners]:
                            if server.name not in zombie_servers:
                                with Action(
                                    f"Found new potential zombie server {server.name}"
                                ):
                                    zombie_servers[server.name] = ZombieServer(
                                        time=time.time(),
                                        server=server,
                                        observed_interval=current_interval,
                                    )
                            zombie_servers[server.name].server = server
                            zombie_servers[
                                server.name
                            ].observed_interval = current_interval

                        else:
                            zombie_servers.pop(server.name, None)

            with Action("Looking for unused runners", level=logging.DEBUG):
                _standby_runners = copy.deepcopy(standby_runners)
                for runner in runners:
                    if runner.status == "online" and not runner.busy:
                        if runner.name.startswith(runner_name_prefix):
                            # skip any specified standby runners
                            if runner.name.startswith(standby_runner_name_prefix):
                                found = False
                                for standby_runner in _standby_runners:
                                    if set(standby_runner.labels).issubset(
                                        set(
                                            [label["name"] for label in runner.labels()]
                                        )
                                    ):
                                        standby_runner.count -= 1
                                        # check if we have too many
                                        if standby_runner.count > -1:
                                            found = True
                                        break
                                if found:
                                    continue
                            if runner.name not in unused_runners:
                                with Action(f"Found new unused runner {runner.name}"):
                                    unused_runners[runner.name] = UnusedRunner(
                                        time=time.time(),
                                        runner=runner,
                                        observed_interval=current_interval,
                                    )
                            unused_runners[runner.name].runner = runner
                            unused_runners[
                                runner.name
                            ].observed_interval = current_interval

            with Action(
                "Checking which powered off servers need to be deleted",
                level=logging.DEBUG,
            ):
                for server_name in list(powered_off_servers.keys()):
                    powered_off_server = powered_off_servers[server_name]

                    if powered_off_server.observed_interval != current_interval:
                        with Action(
                            f"Forgetting about powered off server {server.name}"
                        ):
                            powered_off_servers.pop(server_name)

                    else:
                        if time.time() - powered_off_server.time > max_powered_off_time:
                            with Action(
                                f"Deleting powered off server {server_name}",
                                ignore_fail=True,
                            ) as action:
                                powered_off_server.server.delete()
                                powered_off_servers.pop(server_name)

            with Action(
                "Checking which zombie servers need to be deleted", level=logging.DEBUG
            ):
                for server_name in list(zombie_servers.keys()):
                    zombie_server = zombie_servers[server_name]

                    if zombie_server.observed_interval != current_interval:
                        with Action(f"Forgetting about zombie server {server.name}"):
                            zombie_servers.pop(server_name)

                    else:
                        if (
                            time.time() - zombie_server.time
                            > max_runner_registration_time
                        ):
                            with Action(
                                f"Deleting zombie server {server_name}",
                                ignore_fail=True,
                            ) as action:
                                zombie_server.server.delete()
                                zombie_servers.pop(server_name)

            with Action(
                "Checking which unused runners need to be removed",
                level=logging.DEBUG,
            ):

                for runner_name in list(unused_runners.keys()):
                    unused_runner = unused_runners[runner_name]

                    if unused_runner.observed_interval != current_interval:
                        with Action(f"Forgetting about unused runner {runner_name}"):
                            unused_runners.pop(runner_name)

                    else:
                        if time.time() - unused_runner.time > max_unused_runner_time:
                            runner_server = None

                            with Action(
                                f"Try to find server for the runner {runner_name}",
                                ignore_fail=True,
                            ):
                                runner_server = client.servers.get_by_name(runner_name)

                            if runner_server is not None:
                                with Action(
                                    f"Deleting unused runner server {runner_server.name}",
                                    ignore_fail=True,
                                ):
                                    runner_server.delete()
                                    runner_server = None

                            if runner_server is None:
                                with Action(
                                    f"Removing self-hosted runner {runner_name}",
                                    ignore_fail=True,
                                ):
                                    repo.remove_self_hosted_runner(unused_runner.runner)

        except Exception as exc:
            msg = f"❗ Error: {type(exc).__name__} {exc}"
            if debug:
                logger.exception(f"{msg}\n{exc}")
            else:
                logger.error(msg)

        with Action(f"Sleeping until next interval {interval}s", level=logging.DEBUG):
            time.sleep(interval)
