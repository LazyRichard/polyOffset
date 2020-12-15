from typing import *

from .data import *

class Polyline:
    def __init__(self):
        self._verticies: List[Vertex] = []
        self._is_closed: bool = False

    def add_vertex(self, vert: Vertex):
        if not self.is_closed:
            self._verticies.append(vert)
        else:
            raise ValueError("Polyline is already closed")

    def close(self):
        self._verticies.append(self._verticies[0])
        self._is_closed = True

    @property
    def verticies(self):
        return tuple(zip(*map(lambda x: (x.x, x.y), self._verticies)))

    @property
    def edges(self):
        edges: List[Edge] = []

        for i in range(len(self._verticies) - 1):
            edges.append(Edge(self._verticies[i], self._verticies[i + 1]))

        return edges

    @property
    def is_closed(self):
        return self._is_closed