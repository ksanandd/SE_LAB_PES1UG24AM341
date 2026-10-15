
"""Smart home hub demo with device management and state persistence."""

import json
import os

HUB_HOST = "127.0.0.1"
HUB_PORT = 8080
POWER_USAGE = {"light": 10, "fan": 60, "thermostat": 1500, "tv": 120}
HUB_PASSWORD = os.getenv("SMART_HOME_PASSWORD")
devices = {}


def add_device(device_name, kind, room="Living Room", settings=None):
    """Add a device to the smart home registry."""
    if settings is None:
        settings = {}

    device_settings = settings.copy()
    if kind == "thermostat":
        device_settings.setdefault("temperature", 20)

    devices[device_name] = {
        "kind": kind,
        "room": room,
        "on": False,
        "settings": device_settings,
    }


def toggle_device(device_name):
    """Toggle a registered device and return its new state."""
    if device_name in devices:
        devices[device_name]["on"] = not devices[device_name]["on"]
        return devices[device_name]["on"]

    print("Device not found:", device_name)
    return None


def set_temperature(device_name, value):
    """Set a thermostat temperature within the supported range."""
    device = devices.get(device_name)

    if device is None:
        print("Device not found:", device_name)
        return False

    if device["kind"] != "thermostat":
        print(device_name, "is not a thermostat")
        return False

    device["settings"]["temperature"] = min(max(value, 16), 30)
    return True


def devices_in_room(room):
    """Return device names belonging to a specified room."""
    return [
        name for name, info in devices.items()
        if info["room"] == room
    ]


def power_usage():
    """Calculate the power usage of all switched-on devices."""
    return sum(
        POWER_USAGE.get(info["kind"], 0)
        for info in devices.values()
        if info["on"]
    )


def save_state(file_name="home_state.json"):
    """Save the device registry to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as state_file:
        json.dump(devices, state_file, indent=2)


def hub_address():
    """Return the configured hub address."""
    return f"{HUB_HOST}:{HUB_PORT}"


def main():
    """Run the smart home demonstration."""
    add_device("Ceiling Light", "light")
    add_device("Bedroom Fan", "fan", "Bedroom")
    add_device("Thermostat", "thermostat", "Bedroom")
    add_device("Smart TV", "tv")

    toggle_device("Ceiling Light")
    toggle_device("Thermostat")
    toggle_device("Garage Door")

    set_temperature("Thermostat", 35)
    set_temperature("Ceiling Light", 20)

    print("Bedroom devices:", devices_in_room("Bedroom"))
    print("Current power use (W):", power_usage())
    print("Hub address:", hub_address())
    print("Light settings:", devices["Ceiling Light"]["settings"])
    print(
        "Devices on:",
        [name for name, info in devices.items() if info["on"]],
    )

    save_state()


if __name__ == "__main__":
    main()
