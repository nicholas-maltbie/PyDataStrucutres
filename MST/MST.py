"""

Contains an example of a minimum spanning tree

"""

from Graph import Graph, Edge, Vertex, build_graph
from Heap import Heap
from Partition import Partition

def solve_MST(graph):
    heap = Heap(compare_fn = lambda e1, e2: 1 if e1.obj < e2.obj else -1 if e1.obj > e2.obj else 0)
    
    for edge in graph.edges:
        heap.insert(edge)
    
    part = Partition(value_fn = lambda v: v.obj,
                     hash_fn = lambda v: hash(v.obj))
    
    final = []
    
    while len(heap) > 0:
        edge = heap.pop()
        v1 = edge.v1
        v2 = edge.v2
        if v1 not in part and v2 not in part:
            part.add(v1)
            part.add(v2)
            part.set_union(v1, v2)
            final.append(edge)
        elif (v1 in part) ^ (v2 in part):
            if v1 not in part:
                part.add(v1)
            if v2 not in part:
                part.add(v2)
            part.set_union(v1, v2)
            final.append(edge)
        elif not part.redundant(v1, v2):
            final.append(edge)
            part.set_union(v1, v2)
            
    print(len(final))
    for edge in final:
        print(edge)
    
    return final

if __name__ == "__main__":
    #Graph data, node 1, node 2, cost
    graph_data = \
    """
    1 2 3
    1 3 3
    1 4 3
    1 5 5
    1 6 3
    2 3 4
    2 5 3
    2 6 2
    3 4 1
    3 5 3
    4 5 4
    4 6 2
    5 6 3
    """
    
    solve_MST(build_graph(graph_data))
    
    data_2 = ""
    import random
    for _ in range(10000):
        data_2 += " ".join([str(elem) for elem in[random.randrange(1000), random.randrange(1000), random.randrange(10, 500)]]) + "\n"
    solve_MST(build_graph(data_2))
    
    
