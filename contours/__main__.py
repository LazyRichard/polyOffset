from contours.data import Vertex
from contours import Polyline

poly = Polyline()
poly.add_vertex(Vertex(1, 1))
poly.add_vertex(Vertex(5, 1))
poly.add_vertex(Vertex(5, 5))
poly.add_vertex(Vertex(3, 3))
poly.add_vertex(Vertex(1, 3))
poly.close()

edge = poly.edges[1]
poly.verticies



print("hi")