"""

Contains definition for Hash Table

"""

from List import List

class HashTable:
    """
    
    Hash Table class
    
    """
    
    default_compare = lambda a, b: -1 if a < b else 1 if a > b else 0
    default_disp = lambda x: str(x) + " "
    default_hash = hash
    
    def __init__(self, size, compare_fn = default_compare, hash_fn = default_hash,
            display_fn = default_disp):
        self.table = [None for _ in range(size)]
        self.compare_fn = compare_fn
        self.hash_fn = default_hash
        self.display_fn = default_disp
        
    def add(self, val):
        if self.lookup(val):
            return None
        index = self.hash_fn(val)
        if self.table[index] == None:
            self.table[index] = List(self.compare_fn, self.display_fn)
        table[index].insert(val)
        return val
    
    def lookup(self, val):
        index = self.hash_fn(val)
        return self.table[index] and self.table[index].lookup(val)
    
    def pop(self, val):
        pass

