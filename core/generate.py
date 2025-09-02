# generate.py
import osmnx as ox
import json

# 1️⃣ Generate network
place_name = "Johannesburg, South Africa"
G = ox.graph_from_place(place_name, network_type="drive")

# Keep a subgraph with ~50 nodes for visualization
G = ox.utils_graph.get_largest_component(G, strongly=True)
nodes_list = list(G.nodes)[:50]
G_small = ox.utils_graph.subgraph(G, nodes_list)

# 2️⃣ Extract positions
city_positions = {node: (data['x'], data['y']) for node, data in G_small.nodes(data=True)}

# 3️⃣ Extract adjacency dictionary
city_network = {}
for node, neighbors in G_small.adjacency():
    city_network[node] = {}
    for neighbor, edge_data in neighbors.items():
        distance = edge_data[0].get('length', 1)
        city_network[node][neighbor] = distance

# 4️⃣ Save to files
with open("core/network.py", "w") as f:
    f.write("city_network = " + json.dumps(city_network, indent=4))
with open("core/positions.py", "w") as f:
    f.write("city_positions = " + json.dumps(city_positions, indent=4))

print(f"Generated {len(city_positions)} nodes and saved network/positions!")