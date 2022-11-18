import json
import requests
from typing import List
from geopy import distance


def put_distance(device: dict, coords: tuple) -> None:
    _distance = distance.geodesic(coords, (device["a"], device["n"])).km
    device["distance"] = _distance


def get_nearest_device(devices: List[dict]) -> dict:
    return min(devices, key=lambda d: d["distance"])


def get_location_info(coords: tuple) -> dict:
    res = requests.get("https://www.saveecobot.com/storage/maps_data.js")
    devices: List[dict] = json.loads(res.content)["devices"]

    _ = [put_distance(d, coords) for d in devices]
    air_devices = [d for d in devices if d.get("aqi") and d.get("oldr") == 0]
    radiation_devices = [d for d in devices if d.get("gamma") and d.get("oldr") == 0]

    air_device = get_nearest_device(air_devices)
    radiation_device = get_nearest_device(radiation_devices)

    return {
        "air": {
            "value": air_device["aqi"],
            "distance": round(air_device["distance"], 1),
        },
        "rad": {
            "value": radiation_device["gamma"],
            "distance": round(radiation_device["distance"], 1),
        },
    }
