import heapq
<<<<<<< HEAD

from routing_engine.city_graph import graph
=======
>>>>>>> c7bb686 (Update routing engine and add web dashboard)

def compute_shortest_path(graph, start, end):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == end:
            return path, cost

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return [], float("inf")
