# models/location.py
import json

class Location:
    def __init__(self, location_id, x, y, demand=0):
        self.id = location_id
        self.x = x
        self.y = y
        self.demand = demand

def load_locations(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return [Location(d["id"], d["x"], d["y"], d.get("demand", 0)) for d in data]
