# main.py
from optimization.pso import ParticleSwarmOptimizer
from config import settings
from models.location import load_locations
from models.vehicle import load_vehicles
from visualization.plotter import plot_routes

def main():
    locations = load_locations("data/locations.json")
    vehicles = load_vehicles("data/vehicles.json")

    optimizer = ParticleSwarmOptimizer(
        locations=locations,
        vehicles=vehicles,
        num_particles=settings["num_particles"],
        max_iterations=settings["max_iterations"]
    )

    best_routes, best_cost = optimizer.run()

    print("Best Cost:", best_cost)
    print("Best Routes:", best_routes)

    # Show final best routes
    plot_routes(locations, best_routes, title="Optimal Routes")

if __name__ == "__main__":
    main()
