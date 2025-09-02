import streamlit as st
import matplotlib.pyplot as plt
from core.network import city_network
from core.positions import city_positions

st.title("🚦 RouteAI")
st.write("Plan your route across the city.")

# Dropdowns for start and destination
nodes = list(city_network.keys())
start_node = st.selectbox("Start from:", nodes)
end_node = st.selectbox("Go to:", nodes)

# Button to find route
if st.button("Find Route"):
    st.write(f"Finding route from **{start_node}** to **{end_node}**...")
    # For now, we just display a map; later we integrate ACO routing
    # You can add the routing algorithm here


fig, ax = plt.subplots(figsize=(8, 6))

# Draw nodes
for node, (x, y) in city_positions.items():
    ax.scatter(x, y, color='blue', s=100)
    ax.text(x + 0.2, y + 0.2, node, fontsize=8)

# Draw edges
for node, neighbors in city_network.items():
    x1, y1 = city_positions[node]
    for neighbor in neighbors:
        x2, y2 = city_positions[neighbor]
        ax.plot([x1, x2], [y1, y2], color='gray', linewidth=1)

ax.set_title("City Map")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_aspect('equal')
st.pyplot(fig)