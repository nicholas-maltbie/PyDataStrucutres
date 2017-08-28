from HashTable import HashTable
from Node import Node

default_compare = lambda a, b: -1 if a < b else 1 if a > b else 0

class Partition:
    """
    
    Contains a definition for a partition (inverted tree).
    
    Contains constant time operations for set union of a partioned (all
    disjoint) group of sets.
    
    >>> part = Partition()
    >>> part.add(10)
    >>> part.add(20)
    >>> part.redundant(10, 20)
    False
    >>> part.set_union(10, 20)
    >>> part.redundant(10, 20)
    True
    >>> 
    """
    
    default_display = lambda node: str(node.val)
    default_hash = lambda node: hash(node)
    
    def __init__(self, display_fn = default_display, hash_fn = default_hash,
        value_fn = lambda x: x):
        self.subsets = 0
        self.table = HashTable(compare_fn = lambda a, b: \
            default_compare(value_fn(a.val), value_fn(b.val)), \
            hash_fn = lambda x: hash_fn(x.val), \
            display_fn = display_fn)
    
    def add(self, val):
        if Node(val) not in self.table:
            node = Node(val)
            node.parent = node
            self.table.add(node)
            self.subsets += 1
    
    def __len__(self):
        return self.table.length 
    
    def identify(self, node):
        rep = self.table.lookup(node)
        return rep.identify() if rep != None else None
    
    def set_union(self, a, b):
        p1 = self.identify(self.table.lookup(Node(a)))
        p2 = self.identify(self.table.lookup(Node(b)))
        
        if p1 == p2 or p1 == None or p2 == None:
            return
        if p1.size > p2.size:
            p2.parent = p1
            p1.size += p2.size
        else:
            p1.parent = p2
            p2.size += p1.size
        self.subsets -= 1
    
    def __contains__(self, val):
        return Node(val) in self.table
    
    def redundant(self, a, b):
        return self.identify(self.table.lookup(Node(a))) == \
                self.identify(self.table.lookup(Node(b)))
    
    def __repr__(self):
        return str(self.table)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

