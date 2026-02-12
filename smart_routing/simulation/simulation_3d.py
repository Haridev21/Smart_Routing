# simulation_3d.py

from ursina import *
from routing_engine.routing_algo import compute_shortest_path
from routing_engine.city_graph import graph

app = Ursina()

# -----------------------------
# 3D positions for nodes
# -----------------------------
node_positions = {
    "A": Vec3(-4, 0, 0),
    "B": Vec3(-2, 0, 2),
    "C": Vec3(0, 0, 0),
    "D": Vec3(-2, 0, -2),
    "E": Vec3(2, 0, 2),
    "F": Vec3(4, 0, 0),
}

# -----------------------------
# Draw nodes (intersections)
# -----------------------------
nodes = {}
for name, pos in node_positions.items():
    nodes[name] = Entity(
        model='sphere',
        color=color.azure,
        scale=0.4,
        position=pos
    )

# -----------------------------
# Draw roads
# -----------------------------
for u in graph:
    for v in graph[u]:
        start = node_positions[u]
        end = node_positions[v]

        road = Entity(
            model=Mesh(
                vertices=[start, end],
                mode='line',
                thickness=4
            ),
            color=color.gray
        )

# -----------------------------
# Car class
# -----------------------------
class Car(Entity):
    def __init__(self, start, end, **kwargs):
        super().__init__(
            model='cube',
            color=color.red,
            scale=0.3,
            position=node_positions[start],
            **kwargs
        )

        self.destination = end
        self.path, _ = compute_shortest_path(start, end, {})
        self.target_index = 1
        self.speed = 2

    def update(self):
        if self.target_index >= len(self.path):
            return

        target_node = self.path[self.target_index]
        target_pos = node_positions[target_node]

        direction = (target_pos - self.position).normalized()
        self.position += direction * time.dt * self.speed

        if distance(self.position, target_pos) < 0.1:
            self.target_index += 1

# -----------------------------
# Spawn cars
# -----------------------------
cars = [
    Car("A", "F"),
    Car("B", "F"),
    Car("D", "E")
]

# -----------------------------
# Camera & environment
# -----------------------------
EditorCamera()
Sky()

ground = Entity(
    model='plane',
    scale=20,
    color=color.dark_gray
)

app.run()
