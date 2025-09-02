# generate.py
import osmnx as ox
import random
import json
import os

# Base path to save generated files
base_path = os.path.join(os.getcwd(), "core")
os.makedirs(base_path, exist_ok=True)

# 1️⃣ Use bounding box for central Johannesburg
# Rough bounding box (latitude: -26.0 to -26.3, longitude: 27.9 to 28.1)
north, south = -26.0, -26.3
east, west = 28.1, 27.9

# Generate drive network inside bounding box
G = ox.graph_from_bbox(north, south, east, west, network_type="drive")
G = ox.utils_graph.get_largest_component(G, strongly=True)

# 2️⃣ Sample 50 nodes for visualization
nodes_list = random.sample(list(G.nodes), 50)
G_small = G.subgraph(nodes_list).copy()

# 3️⃣ Extract adjacency dictionary
city_network = {}
for node, neighbors in G_small.adjacency():
    city_network[node] = {}
    for neighbor, edge_data in neighbors.items():
        distance = edge_data[0].get('length', 1)
        city_network[node][neighbor] = distance

# 4️⃣ Extract positions
city_positions = {node: (data['x'], data['y']) for node, data in G_small.nodes(data=True)}

# 5️⃣ Save to files
with open(os.path.join(base_path, "network.py"), "w") as f:
    f.write("city_network = " + json.dumps(city_network, indent=4))

with open(os.path.join(base_path, "positions.py"), "w") as f:
    f.write("city_positions = " + json.dumps(city_positions, indent=4))

print(f"Generated {len(city_positions)} nodes and saved network & positions in {base_path}!")
