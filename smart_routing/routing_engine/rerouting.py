# rerouting.py

from routing_engine.routing_algo import compute_shortest_path

def dynamic_reroute(car, cars_on_edges):
    """
    car = dict with 'start', 'end', 'current', 'current_path'
    cars_on_edges = current cars on each edge
    """
    start = car['current']  # current position
    end = car['end']

    # Calculate new optimal path from current position
    new_path, cost = compute_shortest_path(start, end, cars_on_edges)
    car['current_path'] = new_path
    return car
