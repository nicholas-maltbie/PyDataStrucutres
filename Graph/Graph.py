"""

Contains definitions for parts of a graph.


"""


class Vertex:
    default_compare = lambda a, b: -1 if a < b else 1 if a > b else 0
    
    def __init__(obj = None, index = -1, value_fn = lambda x: x, compare_fn = default_compare):
        self.obj = obj
        self.value_fn = value_fn
        self.compare_fn = compare_fn
        self.neighbors = List(compare_fn)
        self.index = index
    
    def add_neighbor(self, edge)
        self.neighbors.insert(edge)
    
    def get_next_neighbor(self):
        return self.neighbors.next_object()
    
    def get_first_neighbor(self):
        return self.neighbors.start_of_list()
    
    def has_more_neighbors(self):
        return not neighbors.end_of_list()
    
class Edge:
    def __init__(v1, v2, obj = None, value_fn = lambda x: x):
        self.v1 = v1
        self.v2 = v2
        self.obj = None
        self.value_fn = value_fn

class Graph:
    def __init__(self):
        self.nverticies = 0
        self.edges = []
        self.vertices = []

