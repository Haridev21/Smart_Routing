# test_routing.py

from routing_algo import compute_shortest_path
from rerouting import dynamic_reroute


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


path, cost = compute_shortest_path("A", "F", cars_on_edges)
print(f"Optimal path: {path}, total cost: {cost:.2f}")

car = {"start":"A", "end":"F", "current":"A", "current_path":path}

cars_on_edges[("B","C")] = 6  
car = dynamic_reroute(car, cars_on_edges)
print(f"After reroute due to congestion: {car['current_path']}")
