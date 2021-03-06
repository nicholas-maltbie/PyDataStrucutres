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
    20
    >>> table.pop(20)
    20
    >>> table.length
    1
    >>> table.lookup(20)
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
        self.table = [None] * size
        self.compare_fn = compare_fn
        self.size = size
        self.length = 0
        self.hash_function = hash_fn
        self.display_fn = display_fn
    
    def hash_fn(self, val):
        return self.hash_function(val) % self.size
    
    def add(self, val):
        if val in self:
            return
        if len(self) == self.size:
            self.size = self.size * 2
            temp_table = self.table
            self.table = [None] * self.size
            self.length = 0
            for l in temp_table:
                if l:
                    for elem in l:
                        self.add(elem)
            
        index = self.hash_fn(val)
        if self.table[index] == None:
            self.table[index] = List(self.compare_fn, self.display_fn)
        self.length += 1
        self.table[index].insert(val)
    
    def lookup(self, val):
        index = self.hash_fn(val)
        return (self.table[index].lookup(val) if \
                self.table[index] != None and val in self.table[index] else None)
    
    def __iter__(self):
        for i in range(len(self.table)):
            if self.table[i]:
                for val in self.table[i]:
                    yield val

    def __contains__(self, val):
        return self.lookup(val) != None
    
    def display(self):
        return ", ".join([str(l) for l in self.table if l != None and len(l) > 0]) \
                if len(self) > 0 else "<>"
    
    def __repr__(self):
        return self.display()
    
    def __len__(self):
        return self.length
        
    def pop(self, val):
        if val in self:
            self.length -= 1
            return self.table[self.hash_fn(val)].pop(val)
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()

