from typing import *

from enum import Enum
from dataclasses import dataclass, field
import math

class Direction(Enum):
    CW = 0
    CCW = 1

@dataclass(frozen=True)
class Vertex:
    x: float
    y: float

@dataclass(frozen=True)
class Vector:
    x: float
    y: float

    @property
    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    @property
    def matrix(self) -> List[float]:
        return [self.x, self.y]

    @property
    def is_unit(self) -> bool:
        return True if math.isclose(self.magnitude, 1.0) else False

    @property
    def unit_vector(self) -> 'Vector':
        return self if self.is_unit else Vector(self.x / self.magnitude, self.y / self.magnitude)

    @property
    def verticies(self):
        return [0, 0, self.x, self.y]

    # Reference https://gamedev.stackexchange.com/questions/70075/how-can-i-find-the-perpendicular-to-a-2d-vector
    def get_perpendecular(self, maginitute: int, direction: Direction = Direction.CW) -> 'Vector':
        vect: Vector
        if direction == Direction.CW:
            vect = self._perpendicular_cw()
        elif direction == Direction.CCW:
            vect = self._perpendicular_ccw()

        return Vector(vect.x * maginitute, vect.y * maginitute)

    def _perpendicular_cw(self) -> 'Vector':
        hat: Vector = self.unit_vector

        return Vector(hat.y, -hat.x)
    
    def _perpendicular_ccw(self) -> 'Vector':
        hat: Vector = self.unit_vector

        return Vector(-hat.y, hat.x)

    def __add__(self, v: 'Vector'):
        return Vector(x=self.x + v.x, y=self.y + v.y)

    def __sub__(self, v: 'Vector'):
        return Vector(s=self.x - v.x, y=self.y - v.y)

    @classmethod
    def from_vertex(cls, start_vert: Vertex, end_vert: Vertex):
        return cls(
            x=(end_vert.x - start_vert.x),
            y=(end_vert.y - start_vert.y)
        )

@dataclass(frozen=True)
class Edge:
    start: Vertex
    end: Vertex

    @property
    def vector(self):
        return Vector.from_vertex(self.start, self.end)

    def get_offset(self, offset_value: int, direction: Direction = Direction.CW) -> 'Edge':
        perp_vector: Vector = self.vector.get_perpendecular(offset_value, direction)

        return Edge(
            Vertex(self.start.x + perp_vector.x, self.start.y + perp_vector.y),
            Vertex(self.end.x + perp_vector.x, self.end.y + perp_vector.y)
        )

    def get_middle_of(self, loc: float) -> Vertex:
        if loc >= 1.0:
            return self.end
        elif loc <= 0.0:
            return self.start
        else:
            return Vertex(
                self.start.x + (self.end.x - self.start.x) * loc,
                self.start.y + (self.end.y - self.start.y) * loc
            )

    @property
    def verticies(self):
        return ([self.start.x, self.end.x], [self.start.y, self.end.y])