""" aiocomfoconnect CLI application """
from __future__ import annotations

import argparse
import asyncio
import logging
import sys
from asyncio import Future
from typing import Literal

from aiocomfoconnect import DEFAULT_NAME, DEFAULT_PIN, DEFAULT_UUID
from aiocomfoconnect.comfoconnect import ComfoConnect
from aiocomfoconnect.discovery import discover_bridges
from aiocomfoconnect.exceptions import (
    AioComfoConnectNotConnected,
    AioComfoConnectTimeout,
    ComfoConnectNotAllowed,
)
from aiocomfoconnect.sensors import SENSORS

_LOGGER = logging.getLogger(__name__)


async def main(args):
    """Main function."""
    if args.action == "discover":
        await run_discover(args.host)

    elif args.action == "register":
        await run_register(args.host, args.uuid, args.name, args.pin)

    elif args.action == "set-speed":
        await run_set_speed(args.host, args.uuid, args.speed)

    elif args.action == "set-mode":
        await run_set_mode(args.host, args.uuid, args.mode)

    elif args.action == "show-sensors":
        await run_show_sensors(args.host, args.uuid)

    elif args.action == "show-sensor":
        await run_show_sensor(args.host, args.uuid, args.sensor)

    else:
        raise Exception("Unknown action: " + args.action)


async def run_discover(host: str = None):
    """Discover all bridges on the network."""
    bridges = await discover_bridges(host)
    print("Discovered bridges:")
    for bridge in bridges:
        print(bridge)
        print()


async def run_register(host: str, uuid: str, name: str, pin: int):
    """Connect to a bridge."""
    # Discover bridge so we know the UUID
    bridges = await discover_bridges(host)
    if not bridges:
        raise Exception("No bridge found")

    # Connect to the bridge
    comfoconnect = ComfoConnect(bridges[0].host, bridges[0].uuid)

    try:
        # Login with the bridge
        await comfoconnect.connect(uuid)
        print(f"UUID {uuid} is already registered.")

    except ComfoConnectNotAllowed:
        # We probably are not registered yet...
        try:
            await comfoconnect.cmd_register_app(uuid, name, pin)
        except ComfoConnectNotAllowed:
            await comfoconnect.disconnect()
            print("Registration failed. Please check the PIN.")
            sys.exit(1)

        print(f"UUID {uuid} is now registered.")

        # Connect to the bridge
        await comfoconnect.cmd_start_session(True)

    # ListRegisteredApps
    print()
    print("Registered applications:")
    reply = await comfoconnect.cmd_list_registered_apps()
    for app in reply.apps:
        print(f"* {app.uuid.hex()}: {app.devicename}")

    await comfoconnect.disconnect()


async def run_set_speed(host: str, uuid: str, speed: Literal["away", "low", "medium", "high"]):
    """Connect to a bridge."""
    # Discover bridge so we know the UUID
    bridges = await discover_bridges(host)
    if not bridges:
        raise Exception("No bridge found")

    # Connect to the bridge
    comfoconnect = ComfoConnect(bridges[0].host, bridges[0].uuid)
    try:
        await comfoconnect.connect(uuid)
    except ComfoConnectNotAllowed:
        print("Could not connect to bridge. Please register first.")
        sys.exit(1)

    await comfoconnect.set_speed(speed)

    await comfoconnect.disconnect()


async def run_set_mode(host: str, uuid: str, mode: Literal["auto", "manual"]):
    """Connect to a bridge."""
    # Discover bridge so we know the UUID
    bridges = await discover_bridges(host)
    if not bridges:
        raise Exception("No bridge found")

    # Connect to the bridge
    comfoconnect = ComfoConnect(bridges[0].host, bridges[0].uuid)
    try:
        await comfoconnect.connect(uuid)
    except ComfoConnectNotAllowed:
        print("Could not connect to bridge. Please register first.")
        sys.exit(1)

    await comfoconnect.set_mode(mode)

    await comfoconnect.disconnect()


async def run_show_sensors(host: str, uuid: str):
    """Connect to a bridge."""
    # Discover bridge so we know the UUID
    bridges = await discover_bridges(host)
    if not bridges:
        raise Exception("No bridge found")

    def alarm_callback(node_id, errors):
        """Print alarm updates."""
        print(f"Alarm received for Node {node_id}:")
        for error_id, error in errors.items():
            print(f"* {error_id}: {error}")

    def sensor_callback(sensor, value):
        """Print sensor updates."""
        print(f"{sensor.name:>40}: {value} {sensor.unit or ''}")

    # Connect to the bridge
    comfoconnect = ComfoConnect(bridges[0].host, bridges[0].uuid, sensor_callback=sensor_callback, alarm_callback=alarm_callback)
    try:
        await comfoconnect.connect(uuid)
    except ComfoConnectNotAllowed:
        print("Could not connect to bridge. Please register first.")
        sys.exit(1)

    # Register all sensors
    for sensor in SENSORS.values():
        await comfoconnect.register_sensor(sensor)

    try:
        while True:
            # Wait for updates and send a keepalive every 30 seconds
            await asyncio.sleep(30)

            try:
                print("Sending keepalive...")
                # Use cmd_time_request as a keepalive since cmd_keepalive doesn't send back a reply we can wait for
                await comfoconnect.cmd_time_request()

            except (AioComfoConnectNotConnected, AioComfoConnectTimeout):
                # Reconnect when connection has been dropped
                try:
                    await comfoconnect.connect(uuid)
                except AioComfoConnectTimeout:
                    _LOGGER.warning("Connection timed out. Retrying later...")

    except KeyboardInterrupt:
        pass

    print("Disconnecting...")
    await comfoconnect.disconnect()


async def run_show_sensor(host: str, uuid: str, sensor: int):
    """Connect to a bridge."""
    result = Future()

    # Discover bridge so we know the UUID
    bridges = await discover_bridges(host)
    if not bridges:
        raise Exception("No bridge found")

    def sensor_callback(sensor_, value):
        """Print sensor update."""
        result.set_result(value)

    # Connect to the bridge
    comfoconnect = ComfoConnect(bridges[0].host, bridges[0].uuid, sensor_callback=sensor_callback)
    try:
        await comfoconnect.connect(uuid)
    except ComfoConnectNotAllowed:
        print("Could not connect to bridge. Please register first.")
        sys.exit(1)

    if not sensor in SENSORS:
        print(f"Unknown sensor with ID {sensor}")
        sys.exit(1)

    # Register sensors
    await comfoconnect.register_sensor(SENSORS[sensor])

    # Wait for value
    print(await result)

    # Disconnect
    await comfoconnect.disconnect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", "-d", help="Enable debug logging", default=False, action="store_true")
    subparsers = parser.add_subparsers(required=True, dest="action")

    p_discover = subparsers.add_parser("discover", help="discover ComfoConnect LAN C devices on your network")
    p_discover.add_argument("--host", help="Host address of the bridge")

    p_register = subparsers.add_parser("register", help="register on a ComfoConnect LAN C device")
    p_register.add_argument("--pin", help="PIN code to register on the bridge", default=DEFAULT_PIN)
    p_register.add_argument("--host", help="Host address of the bridge")
    p_register.add_argument("--uuid", help="UUID of this app", default=DEFAULT_UUID)
    p_register.add_argument("--name", help="Name of this app", default=DEFAULT_NAME)

    p_set_speed = subparsers.add_parser("set-speed", help="set the fan speed")
    p_set_speed.add_argument("speed", help="Fan speed", choices=["low", "medium", "high", "away"])
    p_set_speed.add_argument("--host", help="Host address of the bridge")
    p_set_speed.add_argument("--uuid", help="UUID of this app", default=DEFAULT_UUID)

    p_set_mode = subparsers.add_parser("set-mode", help="set operation mode")
    p_set_mode.add_argument("mode", help="Operation mode", choices=["auto", "manual"])
    p_set_mode.add_argument("--host", help="Host address of the bridge")
    p_set_mode.add_argument("--uuid", help="UUID of this app", default=DEFAULT_UUID)

    p_sensors = subparsers.add_parser("show-sensors", help="show the sensor values")
    p_sensors.add_argument("--host", help="Host address of the bridge")
    p_sensors.add_argument("--uuid", help="UUID of this app", default=DEFAULT_UUID)

    p_sensor = subparsers.add_parser("show-sensor", help="show a single sensor value")
    p_sensor.add_argument("sensor", help="The ID of the sensor", type=int)
    p_sensor.add_argument("--host", help="Host address of the bridge")
    p_sensor.add_argument("--uuid", help="UUID of this app", default=DEFAULT_UUID)

    arguments = parser.parse_args()

    if arguments.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    try:
        asyncio.run(main(arguments), debug=True)
    except KeyboardInterrupt:
        pass
