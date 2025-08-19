import random
from .fitness import evaluate_solution

class Particle:
    def __init__(self, num_locations, num_vehicles):
        # Random initial solution
        locations = list(range(1, num_locations))  # Exclude depot (0)
        random.shuffle(locations)
        self.position = self._split_routes(locations, num_vehicles)
        self.best_position = list(self.position)
        self.best_score = float("inf")
        self.velocity = []  # Will hold swaps

    def _split_routes(self, locations, num_vehicles):
        """ Randomly assign locations to vehicles """
        return [locations[i::num_vehicles] for i in range(num_vehicles)]

class ParticleSwarmOptimizer:
    def __init__(self, locations, vehicles, num_particles, max_iterations):
        self.locations = locations
        self.vehicles = vehicles
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.swarm = [Particle(len(locations), len(vehicles)) for _ in range(num_particles)]
        self.global_best_position = None
        self.global_best_score = float("inf")

    def run(self):
        for iteration in range(self.max_iterations):
            for particle in self.swarm:
                score = evaluate_solution(particle.position, self.locations)

                # Update personal best
                if score < particle.best_score:
                    particle.best_score = score
                    particle.best_position = list(particle.position)

                # Update global best
                if score < self.global_best_score:
                    self.global_best_score = score
                    self.global_best_position = list(particle.position)

            # TODO: Update velocity + move particles

        return self.global_best_position, self.global_best_score
