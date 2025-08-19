# app.py
import streamlit as st
import matplotlib.pyplot as plt
from optimization.pso import ParticleSwarmOptimizer
from config import settings
from models.location import load_locations
from models.vehicle import load_vehicles
from visualization.plotter import plot_routes

st.title("🚚 RouteAI - Particle Swarm Optimization")

# Load data
locations = load_locations("data/locations.json")
vehicles = load_vehicles("data/vehicles.json")

# Sidebar controls
num_particles = st.sidebar.slider("Number of Particles", 10, 100, settings["num_particles"])
max_iterations = st.sidebar.slider("Max Iterations", 10, 500, settings["max_iterations"])

if st.button("Run Optimization"):
    optimizer = ParticleSwarmOptimizer(
        locations=locations,
        vehicles=vehicles,
        num_particles=num_particles,
        max_iterations=max_iterations
    )

    best_routes, best_cost = optimizer.run()

    st.success(f"Best Cost: {best_cost}")

    # Plot with matplotlib
    fig, ax = plt.subplots(figsize=(6,6))
    plot_routes(locations, best_routes, ax=ax, title="Optimal Routes")
    st.pyplot(fig)
