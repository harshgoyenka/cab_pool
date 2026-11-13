import json
from methods import Cab, RideRequest

cabs_file = "cabs.json"
requests_file = "pending_requests.json"


def load_cabs():
    try:
        with open(cabs_file, "r") as f:
            data = json.load(f)
        return [Cab.from_dict(i) for i in data]
    except Exception as e:
        print(f"Error reading '{cabs_file}': {e}. Starting with an empty cab list.")
        return []


def save_cabs(cabs):
    with open(cabs_file, "w") as f:
        json.dump([cab.to_dict() for cab in cabs], f, indent=2)


def load_requests():
    try:
        with open(requests_file, "r") as f:
            data = json.load(f)
        return [RideRequest.from_dict(i) for i in data]
    except Exception as e:
        print(f"Warning: Could not load saved requests ({e}). Starting fresh.")
        return []


def save_requests(requests):
    with open(requests_file, "w") as f:
        json.dump([i.to_dict() for i in requests], f, indent=2)