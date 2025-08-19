import math

def euclidean_distance(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def total_route_distance(route, locations):
    distance = 0
    for i in range(len(route) - 1):
        distance += euclidean_distance(locations[route[i]], locations[route[i+1]])
    return distance
