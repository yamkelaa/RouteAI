# generate.py
import osmnx as ox
import json
import os
import networkx as nx

# Create core directory if it doesn't exist
os.makedirs("core", exist_ok=True)

# 1️⃣ Generate network - use the new OSMnx API
try:
    # For newer versions of OSMnx, use the correct syntax
    north, south, east, west = -26.10, -26.25, 28.15, 27.90
    G = ox.graph_from_bbox(north=north, south=south, east=east, west=west, network_type="drive")
    print("Successfully generated graph from bounding box")
    
except Exception as e:
    print(f"Error with OSMnx: {e}")
    print("Generating synthetic network as fallback...")
    
    # Create a simple grid network as fallback
    G = nx.grid_2d_graph(7, 7)  # 7x7 grid = 49 nodes

    # Convert to proper node IDs and add positions
    G_small = nx.Graph()
    city_positions = {}
    city_network = {}

    node_id = 0
    for (i, j) in G.nodes():
        G_small.add_node(node_id)
        city_positions[node_id] = (i * 100, j * 100)  # Simple coordinates
        node_id += 1

    # Add edges with distances
    for (i1, j1), (i2, j2) in G.edges():
        node1 = list(city_positions.keys())[list(G.nodes()).index((i1, j1))]
        node2 = list(city_positions.keys())[list(G.nodes()).index((i2, j2))]
        distance = ((i2 - i1) ** 2 + (j2 - j1) ** 2) ** 0.5 * 100
        G_small.add_edge(node1, node2, length=distance)

    # Build adjacency dictionary
    for node, neighbors in G_small.adjacency():
        city_network[node] = {}
        for neighbor, edge_data in neighbors.items():
            distance = edge_data.get('length', 1)
            city_network[node][neighbor] = distance

    # Save to files
    with open("core/network.py", "w") as f:
        f.write("city_network = " + json.dumps(city_network, indent=4))
        
    with open("core/positions.py", "w") as f:
        f.write("city_positions = " + json.dumps(city_positions, indent=4))

    print(f"Generated synthetic network with {len(city_positions)} nodes!")
    exit()

# If OSMnx worked, process the real network
# Keep a subgraph with ~50 nodes for visualization
G = ox.utils_graph.get_largest_component(G, strongly=True)
nodes_list = list(G.nodes)[:50]
G_small = G.subgraph(nodes_list)

# 2️⃣ Extract positions
city_positions = {}
for node, data in G_small.nodes(data=True):
    city_positions[node] = (data['x'], data['y'])

# 3️⃣ Extract adjacency dictionary
city_network = {}
for node, neighbors in G_small.adjacency():
    city_network[node] = {}
    for neighbor, edge_data in neighbors.items():
        # Get the first edge (there might be multiple edges between nodes)
        first_edge = next(iter(edge_data.values()))
        distance = first_edge.get('length', 1)
        city_network[node][neighbor] = distance

# 4️⃣ Save to files
with open("core/network.py", "w") as f:
    f.write("city_network = " + json.dumps(city_network, indent=4))
    
with open("core/positions.py", "w") as f:
    f.write("city_positions = " + json.dumps(city_positions, indent=4))

print(f"Generated {len(city_positions)} nodes and saved network/positions!")