"""

Contains definitions for parts of a graph.

>>> v1 = Vertex(1)
>>> v2 = Vertex(2)
>>> e = Edge(v1, v2)
>>> graph = Graph([e], [v1, v2])
>>> len(graph.get_vertex(1).neighbors)
1
>>> 
"""

from HashTable import HashTable
from List import List

class Vertex:
    default_compare = lambda a, b: -1 if a < b else 1 if a > b else 0
    
    def __init__(self, obj = None, index = -1, value_fn = lambda x: x, \
            compare_fn = default_compare):
        self.obj = obj
        self.value_fn = value_fn
        self.compare_fn = compare_fn
        self.neighbors = List(compare_fn=compare_fn)
        self.index = index
    
    def add_neighbor(self, edge):
        self.neighbors.insert(edge)
    
    def get_next_neighbor(self):
        return self.neighbors.next_object()
    
    def get_first_neighbor(self):
        return self.neighbors.start_of_list()
    
    def has_more_neighbors(self):
        return not neighbors.end_of_list()
    
    def __repr__(self):
        return str(self.obj)
    
class Edge:
    def __init__(self, v1, v2, obj = None, value_fn = lambda x: x):
        self.v1 = v1
        self.v2 = v2
        self.obj = obj
        self.value_fn = value_fn
        
    def __repr__(self):
        return ", ".join([str(self.v1), str(self.v2), str(self.obj)])

class Graph:
    def __init__(self, edges = List(), vertices = List()):
        self.edges = List()
        self.vertices = HashTable(hash_fn = lambda x: hash(x.obj), \
            compare_fn = lambda a, b: -1 if a.obj < b.obj else 1 if a.obj > b.obj else 0)
        for v in vertices:
            self.add_vertex(v)
        for edge in edges:
            self.add_edge(edge)
    
    def add_edge(self, edge):
        self.edges.insert(edge)
        self.get_vertex(edge.v1.obj).add_neighbor(edge)
        self.get_vertex(edge.v2.obj).add_neighbor(edge)
    
    def add_vertex(self, vertex):
        self.vertices.add(vertex)
    
    def get_vertex(self, obj):
        return self.vertices.lookup(Vertex(obj))

def build_graph(graph_data):
    vertices = HashTable(compare_fn = lambda a, b: 1 if a.obj > b.obj else 
                                                   -1 if a.obj < b.obj else
                                                   0)
    edges = List()
    for line in graph_data.split('\n'):
        if line.strip():
            v1, v2, cost = (int(val) for val in line.strip().split(' '))
            vertices.add(Vertex(v1))
            vertices.add(Vertex(v2))
            edges.insert(Edge(Vertex(v1), Vertex(v2), cost))

    return Graph(edges, vertices)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

        
