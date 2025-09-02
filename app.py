# app.py
import streamlit as st
import matplotlib.pyplot as plt
from core.network import city_network
from core.positions import city_positions
from core.traffic import apply_traffic

st.title("🚦 RouteAI")
st.write("Plan your route across the city.")

# Apply dynamic traffic before plotting
apply_traffic(city_network)

# Dropdowns for start and destination
nodes = list(city_network.keys())
start_node = st.selectbox("Start from:", nodes)
end_node = st.selectbox("Go to:", nodes)

# Button to find route
if st.button("Find Route"):
    st.write(f"Finding route from **{start_node}** to **{end_node}**...")
    # Routing algorithm can be integrated here

# Plot city map with wider figure and smaller font
fig, ax = plt.subplots(figsize=(14, 6))  # wider (14) and shorter (6)

# Draw nodes
for node, (x, y) in city_positions.items():
    ax.scatter(x, y, color='blue', s=80)  # slightly smaller node marker
    ax.text(x + 0.3, y + 0.3, node, fontsize=8)  # smaller font

# Draw edges
for node, neighbors in city_network.items():
    x1, y1 = city_positions[node]
    for neighbor in neighbors:
        x2, y2 = city_positions[neighbor]
        ax.plot([x1, x2], [y1, y2], color='gray', linewidth=0.8)  # thinner edges

# Map styling
ax.set_title("City Map", fontsize=14)
ax.set_xlabel("X", fontsize=10)
ax.set_ylabel("Y", fontsize=10)
ax.set_aspect('equal')

st.pyplot(fig)
