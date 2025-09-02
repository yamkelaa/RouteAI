import random
import json

# Define categories and counts
categories = {
    "Residential": 80,
    "School": 35,
    "Park": 25,
    "Garage": 25,
    "Hospital": 15,
    "Office": 25,
    "TransportHub": 15,
    "PoliceStation": 20
}

# 1️⃣ Generate node names
nodes = []
for cat, count in categories.items():
    for i in range(1, count + 1):
        nodes.append(f"{cat}_{i}")


# 2️⃣ Generate network edges
network = {}
for node in nodes:
    num_neighbors = random.randint(2, 5)
    neighbors = random.sample([n for n in nodes if n != node], num_neighbors)
    network[node] = {neighbor: random.randint(1, 15) for neighbor in neighbors}

# 3️⃣ Adding some dynamic road features
for node, edges in network.items():
    for neighbor in edges:
        # 20% chance to simulate a pothole / traffic congestion
        if random.random() < 0.2:
            edges[neighbor] += random.randint(1, 5)

# 4️⃣ Generate coordinates for plotting
positions = {node: (random.uniform(0, 100), random.uniform(0, 100)) for node in nodes}

# 5️⃣ Save to files
with open("network.py", "w") as f:
    f.write("city_network = " + json.dumps(network, indent=4))

with open("positions.py", "w") as f:
    f.write("city_positions = " + json.dumps(positions, indent=4))

print(f"Generated {len(nodes)} nodes with network and coordinates!")