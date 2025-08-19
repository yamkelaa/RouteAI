# models/vehicle.py
import json

class Vehicle:
    def __init__(self, vehicle_id, capacity=100):
        self.id = vehicle_id
        self.capacity = capacity

def load_vehicles(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return [Vehicle(d["id"], d.get("capacity", 100)) for d in data]
