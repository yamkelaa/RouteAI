import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import math
from core.network import city_network
from core.positions import city_positions

st.set_page_config(page_title="RouteAI", layout="wide")

st.title("🚦 RouteAI")
st.write("Dynamic traffic-aware routing across the city.")

# Create two columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    # Dropdowns for node selection
    nodes = list(city_network.keys())
    start_node = st.selectbox("📍 Start from:", nodes, index=nodes.index("Rosebank"))
    end_node = st.selectbox("🎯 Go to:", nodes, index=nodes.index("Sandton"))
    
    # Algorithm selection
    algorithm = st.radio("Routing Algorithm:", 
                        ["Dijkstra's Algorithm", "A* Algorithm", "Bellman-Ford Algorithm"])
    
    # Additional options
    show_distances = st.checkbox("Show distances on edges", value=True)
    show_all_nodes = st.checkbox("Show all node labels", value=True)
    
    if st.button("🚀 Find Shortest Route"):
        # Find shortest path
        try:
            G = nx.Graph()
            for node, neighbors in city_network.items():
                for neighbor, weight in neighbors.items():
                    G.add_edge(node, neighbor, weight=weight)
            
            if algorithm == "Dijkstra's Algorithm":
                path = nx.dijkstra_path(G, start_node, end_node)
                path_length = nx.dijkstra_path_length(G, start_node, end_node)
            elif algorithm == "A* Algorithm":
                # Simple heuristic for A* (Euclidean distance based on positions)
                def heuristic(u, v):
                    x1, y1 = city_positions[u]
                    x2, y2 = city_positions[v]
                    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                
                path = nx.astar_path(G, start_node, end_node, heuristic=heuristic)
                path_length = nx.astar_path_length(G, start_node, end_node, heuristic=heuristic)
            else:  # Bellman-Ford
                path = nx.bellman_ford_path(G, start_node, end_node)
                path_length = nx.bellman_ford_path_length(G, start_node, end_node)
            
            st.success(f"Shortest route found! Total distance: {path_length} km")
            st.write("**Route:**", " → ".join(path))
            
        except nx.NetworkXNoPath:
            st.error("No path exists between the selected locations.")
    
    # Display graph info
    st.subheader("Network Information")
    st.write(f"Total nodes: {len(city_network)}")
    st.write(f"Total edges: {sum(len(neighbors) for neighbors in city_network.values()) // 2}")

with col2:
    # Build Graph
    G = nx.Graph()
    for node, neighbors in city_network.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    # Create the plot with larger figure size
    fig, ax = plt.subplots(figsize=(14, 12))
    
    # Draw the graph
    nx.draw_networkx_edges(G, pos=city_positions, ax=ax, edge_color="gray", width=1.5, alpha=0.7)
    
    # Draw all nodes
    nx.draw_networkx_nodes(G, pos=city_positions, ax=ax, node_size=500, 
                          node_color="lightblue", edgecolors="black", linewidths=1)
    
    # Highlight start and end nodes
    nx.draw_networkx_nodes(G, pos=city_positions, nodelist=[start_node], 
                          node_color="green", node_size=700, ax=ax)
    nx.draw_networkx_nodes(G, pos=city_positions, nodelist=[end_node], 
                          node_color="red", node_size=700, ax=ax)
    
    # Draw path if calculated
    if 'path' in locals():
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, pos=city_positions, edgelist=path_edges,
                              ax=ax, edge_color="orange", width=3)
        nx.draw_networkx_nodes(G, pos=city_positions, nodelist=path,
                              node_color="orange", node_size=500, ax=ax)
    
    # Draw labels with larger font
    if show_all_nodes:
        nx.draw_networkx_labels(G, pos=city_positions, ax=ax, font_size=10, font_weight="bold")
    
    # Draw edge labels if requested - with error handling
    if show_distances:
        edge_labels = nx.get_edge_attributes(G, 'weight')
        # Use a simpler approach for edge labels to avoid the error
        for edge, weight in edge_labels.items():
            x1, y1 = city_positions[edge[0]]
            x2, y2 = city_positions[edge[1]]
            ax.text((x1 + x2) / 2, (y1 + y2) / 2, str(weight), 
                   fontsize=8, ha='center', va='center',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    ax.set_title("Johannesburg City Network", fontsize=18)
    ax.set_facecolor('#f5f5f5')
    ax.axis("off")
    
    # Set appropriate limits for the massively expanded coordinate system
    ax.set_xlim(0, 140)
    ax.set_ylim(0, 140)
    
    # Display the plot
    st.pyplot(fig)

# Add some information about the app
st.subheader("About RouteAI")
st.write("""
RouteAI is a traffic-aware routing system that helps you find the shortest path between 
locations in Johannesburg. The map shows various points of interest including:
- 🏘️ Suburbs and residential areas
- 🛣️ Major intersections and highways
- 🏞️ Parks and recreational areas
- 🏫 Schools and educational institutions
- 🏥 Hospitals and healthcare facilities
- ⛽ Fuel stations and garages
- 🏢 Office and commercial areas
- 🚉 Transport hubs and airports
""")