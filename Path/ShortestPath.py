"""
Contains an eample of finding the shortest path in a 
graph by use of a priority queue.
"""

from Heap import Heap
from HashTable import HashTable
from Graph import build_graph
from List import List

class Path:
    def __init__(self, other_path = None):
        self.edges = List()
        if other_path != None:
            for edge in other_path.edges:
                self.add_edge(edge, None)
            self.end = other_path.end
        else:
            self.end = None
        
    def add_edge(self, edge, target):
        self.edges.insert(edge)
        self.end = target
    
    def get_cost(self):
        return sum([edge.obj for edge in self.edges])
    
    def __repr__(self):
        return "\n".join([str(edge) for edge in self.edges]) + "\n" + str(self.get_cost())

def shortest_path(graph, start, end):
    queue = Heap(compare_fn= lambda p1, p2:
                                1 if p1.get_cost() < p2.get_cost() else
                               -1 if p1.get_cost() > p2.get_cost() else 0)
    checked = HashTable()    
    checked.add(start)
    for edge in graph.get_vertex(start).neighbors:
        path = Path()
        endpt = edge.v1.obj
        if edge.v1.obj == start:
            endpt = edge.v2.obj
        path.add_edge(edge, endpt)
        queue.insert(path)
    
    while len(queue) > 0:
        path = queue.pop()
        first = path.end
        if first not in checked:
            checked.add(first)
            for edge in graph.get_vertex(first).neighbors:
                path2 = Path(path)
                other = edge.v1.obj
                if edge.v1.obj == first:
                    other = edge.v2.obj
                path2.add_edge(edge, other)
                if other == end:
                    return path2
                else:
                    queue.insert(path2)
    return None
            
        
    
if __name__ == "__main__":
    #Graph data, node 1, node 2, cost
    graph_data = \
    """
    1 2 3
    1 4 3
    2 3 4
    2 5 3
    4 5 4
    4 6 2
    5 6 3
    """
    
    path = shortest_path(build_graph(graph_data), 3, 4)
    print("Final path edges")
    print(path)
    
