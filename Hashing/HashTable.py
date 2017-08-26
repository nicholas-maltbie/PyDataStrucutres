"""

Contains definition for Hash Table

"""

from List import List

class HashTable:
    """
    
    Hash Table class
    
    >>> table = HashTable(100)
    >>> table.add(20)
    >>> table.add(50)
    >>> table.length
    2
    >>> table.lookup(20)
    True
    >>> table.pop(20)
    20
    >>> table.length
    1
    >>> table.lookup(20)
    False
    >>> 50 in table
    True
    >>> len(table)
    1
    >>> 
    """
    
    default_compare = lambda a, b: -1 if a < b else 1 if a > b else 0
    default_disp = lambda x: str(x) + " "
    default_hash = hash
    
    def __init__(self, size = 10, compare_fn = default_compare, hash_fn = default_hash,
            display_fn = default_disp):
        self.table = [None for _ in range(size)]
        self.compare_fn = compare_fn
        self.size = size
        self.length = 0
        self.hash_fn = lambda v: hash_fn(v) % size
        self.display_fn = display_fn
        
    def add(self, val):
        if self.lookup(val):
            return
        index = self.hash_fn(val)
        if self.table[index] == None:
            self.table[index] = List(self.compare_fn, self.display_fn)
            self.length += 1
        self.table[index].insert(val)
    
    def lookup(self, val):
        index = self.hash_fn(val)
        return self.table[index] != None and self.table[index].lookup(val)
    
    def __contains__(self, val):
        return self.lookup(val)
    
    def display(self):
        return ", ".join([str(l) for l in self.table if l != None and len(l) > 0]) \
                if len(self) > 0 else "<>"
    
    def __repr__(self):
        return self.display()
    
    def __len__(self):
        return self.length
        
    def pop(self, val):
        if self.lookup(val):
            self.length -= 1
            return self.table[self.hash_fn(val)].pop(val)
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()

