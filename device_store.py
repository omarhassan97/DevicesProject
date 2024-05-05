import json
import os
from typing import List, Dict

DEVICE_STORE_FILE = "devices.json"

def load_devices() -> List[Dict]:
    if os.path.exists(DEVICE_STORE_FILE):
        with open(DEVICE_STORE_FILE, "r") as file:
            return json.load(file)
    return []

def save_devices(devices: List[Dict]):
    with open(DEVICE_STORE_FILE, "w") as file:
        json.dump(devices, file, indent=2)

def get_device_by_id(device_id: int) -> Dict:
    devices = load_devices()
    for device in devices:
        if device["id"] == device_id:
            return device
    return None

def add_device(device: Dict):
    devices = load_devices()
    devices.append(device)
    save_devices(devices)
