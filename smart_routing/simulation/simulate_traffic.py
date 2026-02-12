# simulate_traffic.py

import matplotlib.pyplot as plt
import networkx as nx

from routing_engine.routing_algo import compute_shortest_path
from routing_engine.rerouting import dynamic_reroute
from routing_engine.city_graph import graph

# -----------------------------
# Setup visualization window
# -----------------------------
plt.ion()  # interactive mode ON
plt.figure(figsize=(8, 6))

# -----------------------------
# Initialize cars
# -----------------------------
cars = [
    {"id": 1, "start": "A", "end": "F", "current": "A", "current_path": []},
    {"id": 2, "start": "B", "end": "F", "current": "B", "current_path": []},
    {"id": 3, "start": "A", "end": "E", "current": "A", "current_path": []}
]

# Track congestion
cars_on_edges = {(u, v): 0 for u in graph for v in graph[u]}

# Assign initial routes
for car in cars:
    path, cost = compute_shortest_path(car["current"], car["end"], cars_on_edges)
    car["current_path"] = path

# -----------------------------
# Visualization function
# -----------------------------
def plot_city(cars):
    plt.clf()

    G = nx.DiGraph()

    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v)

    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=700)

    # Draw cars
    for car in cars:
        node = car["current"]
        x, y = pos[node]
        plt.scatter(x, y, s=200)

    plt.pause(0.8)

# -----------------------------
# Simulation loop
# -----------------------------
steps = 15
congestion_threshold = 3

print("Starting simulation...\n")

for t in range(steps):
    print("Time step:", t)

    # Move cars
    for car in cars:
        path = car["current_path"]

        if len(path) > 1:
            edge = (path[0], path[1])
            cars_on_edges[edge] += 1

            car["current"] = path[1]
            car["current_path"] = path[1:]

    # Print status
    for car in cars:
        print("Car", car["id"], "at", car["current"], "| Path:", car["current_path"])

    # Rerouting logic
    for car in cars:
        if len(car["current_path"]) > 1:
            edge = (car["current_path"][0], car["current_path"][1])

            if cars_on_edges.get(edge, 0) > congestion_threshold:
                dynamic_reroute(car, cars_on_edges)
                print("Car", car["id"], "rerouted →", car["current_path"])

    # Reduce congestion
    for edge in cars_on_edges:
        if cars_on_edges[edge] > 0:
            cars_on_edges[edge] -= 1

    # Draw animation
    plot_city(cars)

print("\nSimulation finished.")

plt.ioff()
plt.show()
