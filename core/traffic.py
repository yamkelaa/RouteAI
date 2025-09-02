# core/traffic.py
import random

def apply_traffic(city_network, congestion_chance=0.2, max_increase=10):
    """
    Randomly increase edge weights to simulate traffic/potholes.
    """
    for node, neighbors in city_network.items():
        for neighbor in neighbors:
            if random.random() < congestion_chance:
                city_network[node][neighbor] += random.randint(1, max_increase)
