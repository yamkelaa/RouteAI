import random

def apply_traffic(city_network, traffic_chance=0.2, max_delay=5):
    """
    Randomly increases edge weights to simulate traffic or potholes.
    """
    for node, neighbors in city_network.items():
        for neighbor in neighbors:
            if random.random() < traffic_chance:
                neighbors[neighbor] += random.randint(1, max_delay)
