# test_routing.py

from routing_algo import compute_shortest_path
from rerouting import dynamic_reroute

# Simulated number of cars on each edge
cars_on_edges = {
    ("A","B"): 2,
    ("B","C"): 4,
    ("C","F"): 1,
    ("A","D"): 1,
    ("D","E"): 0,
    ("E","F"): 2,
    ("B","E"): 3,
    ("C","E"): 1
}

# Test single-car routing
path, cost = compute_shortest_path("A", "F", cars_on_edges)
print(f"Optimal path: {path}, total cost: {cost:.2f}")

# Test dynamic rerouting
car = {"start":"A", "end":"F", "current":"A", "current_path":path}

# Simulate congestion changed
cars_on_edges[("B","C")] = 6  # new heavy traffic
car = dynamic_reroute(car, cars_on_edges)
print(f"After reroute due to congestion: {car['current_path']}")
