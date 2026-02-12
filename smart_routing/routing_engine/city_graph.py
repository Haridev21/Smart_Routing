# city_graph.py

# Graph as adjacency list with distances
graph = {
    "A": {"B": 10, "D": 15},
    "B": {"C": 8, "E": 7},
    "C": {"F": 12, "E": 5},
    "D": {"E": 10},
    "E": {"F": 10},
    "F": {}
}

# Function to get neighbors
def get_neighbors(node):
    return graph.get(node, {})
