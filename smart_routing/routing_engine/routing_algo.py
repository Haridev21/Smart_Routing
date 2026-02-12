# routing_algo.py

import heapq
#from city_graph import graph
from routing_engine.city_graph import graph

def predict_congestion_stub(cars_on_edge):
    """
    Simple congestion estimator:
    - 0 cars = 0.0 congestion
    - 1-2 cars = 0.2
    - 3-4 cars = 0.6
    - 5+ cars = 1.0
    """
    if cars_on_edge == 0:
        return 0.0
    elif cars_on_edge <= 2:
        return 0.2
    elif cars_on_edge <= 4:
        return 0.6
    else:
        return 1.0

def compute_shortest_path(start, end, cars_on_edges):
    """
    start = starting node
    end = ending node
    cars_on_edges = dict with current cars on each edge, e.g., {("A","B"): 3, ("B","C"):2,...}
    """
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == end:
            return path, cost

        if node in visited:
            continue
        visited.add(node)

        for neighbor, distance in graph.get(node, {}).items():
            edge = (node, neighbor)
            cars = cars_on_edges.get(edge, 0)
            congestion = predict_congestion_stub(cars)
            edge_weight = distance * (1 + congestion)
            heapq.heappush(queue, (cost + edge_weight, neighbor, path + [neighbor]))

    return None, float('inf')
