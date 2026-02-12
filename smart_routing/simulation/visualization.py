# visualization.py

import matplotlib.pyplot as plt
import networkx as nx
from routing_engine.city_graph import graph

def plot_city(cars_positions):
    G = nx.DiGraph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v, weight=graph[u][v]['distance'])
    
    pos = nx.spring_layout(G)  # positions for nodes
    plt.figure(figsize=(8,6))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightgreen")
    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15)
    
    # Draw cars
    for car in cars_positions:
        node = car['current']
        plt.scatter(*pos[node], s=200, label=f"Car {car['id']}")
    
    plt.legend()
    plt.show()
