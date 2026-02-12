import random

def generate_traffic_graph():
    base_graph = {
        "A": {"B": 10, "C": 15},
        "B": {"A": 10, "D": 12, "E": 15},
        "C": {"A": 15, "D": 10},
        "D": {"B": 12, "C": 10, "F": 5},
        "E": {"B": 15, "F": 10},
        "F": {"D": 5, "E": 10}
    }

<<<<<<< HEAD

def get_neighbors(node):
    return graph.get(node, {})
=======
    graph = {}

    for node in base_graph:
        graph[node] = {}

        for neighbor, cost in base_graph[node].items():
            congestion = random.uniform(1.0, 2.5)
            graph[node][neighbor] = cost * congestion

    return graph
>>>>>>> c7bb686 (Update routing engine and add web dashboard)
