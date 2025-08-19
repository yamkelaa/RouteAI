from .utils import total_route_distance

def evaluate_solution(routes, locations):
    """ Fitness = total distance of all vehicle routes """
    total = 0
    for route in routes:
        total += total_route_distance(route, locations)
    return total
