# dataset_generator.py

import random
import pandas as pd

# --------------------------
# Define city graph
# --------------------------
# Nodes = intersections
nodes = ["A", "B", "C", "D", "E", "F"]

# Edges = roads with distance
edges = {
    ("A", "B"): 10,
    ("B", "C"): 8,
    ("C", "F"): 12,
    ("A", "D"): 15,
    ("D", "E"): 10,
    ("E", "F"): 10,
    ("B", "E"): 7,
    ("C", "E"): 5,
}

# --------------------------
# Simulation parameters
# --------------------------
time_steps = 50          # e.g., 50 minutes
max_cars_per_step = 5    # new cars spawning per step

data = []

for t in range(time_steps):
    # Simulate cars on each edge
    for edge in edges:
        # Random traffic load
        cars_on_edge = random.randint(0, max_cars_per_step)
        distance = edges[edge]

        # Congestion = cars / max capacity (assume capacity=5 per edge)
        congestion = min(1.0, cars_on_edge / max_cars_per_step)

        data.append({
            "time": t,
            "edge_start": edge[0],
            "edge_end": edge[1],
            "distance": distance,
            "cars": cars_on_edge,
            "congestion": congestion
        })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("traffic_dataset.csv", index=False)
print("Dataset generated: traffic_dataset.csv")
