import math

def get_parent(node):
    return (node - 1) // 2

def get_left(node):
    return node * 2 + 1

def get_left(node):
    return node * 2 + 1

def get_right(node):
    return node * 2 + 2

class Heap:
    """

    Contains a definition for a Heap
    
    >>> heap = Heap()
    >>> heap.insert(10)
    >>> heap.insert(100)
    >>> heap.top()
    100
    >>> heap.pop()
    100
    >>> heap.top()
    10
    >>> 
    """
    default_compare = lambda a, b: -1 if a < b else 1 if a > b else 0
    
    def __init__(self, layers=3, compare_fn=default_compare):
        self.elems = [None] * ((2 ** layers) - 1)
        self.compare_fn = compare_fn
        self.layers = layers
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def insert(self, val):
        if val != None:
            if len(self) == len(self.elems):
                self.elems = self.elems + [None] * (2 ** self.layers)
                self.layers += 1
            self.elems[len(self)] = val
            self.comp_up(len(self))
            self.length += 1
        
    def top(self):
        return self.elems[0]
    
    def pop(self):
        if len(self) > 0:
            obj = self.elems[0]
            self.length -= 1
            self.elems[0] = self.elems[len(self)]
            self.elems[len(self)] = None
            self.comp_down(0)
            return obj
        
    def __len__(self):
        return self.length
    
    def comp_up(self, node):
        parent = get_parent(node)
        if node == 0 or self.compare_fn(self.elems[node], self.elems[parent]) < 1:
            return
        else:
            temp = self.elems[node]
            self.elems[node] = self.elems[parent]
            self.elems[parent] = temp
            self.comp_up(parent)
    
    def comp_down(self, node):
        c1, c2 = get_left(node), get_right(node)
        if c1 > len(self.elems) or c2 > len(self.elems):
            return 
        if self.elems[c1] != None and \
            (self.elems[node] == None or \
             self.compare_fn(self.elems[c1], self.elems[node]) == 1) and \
            (self.elems[c2] == None or self.compare_fn(self.elems[c1], self.elems[c2]) == 1):
            temp = self.elems[node]
            self.elems[node] = self.elems[c1]
            self.elems[c1] = temp
            self.comp_down(c1)
        elif self.elems[c2] != None and \
            (self.elems[node] == None or \
             self.compare_fn(self.elems[c2], self.elems[node]) == 1) and \
            (self.elems[c1] == None or self.compare_fn(self.elems[c2], self.elems[c1]) >= 0):
            temp = self.elems[node]
            self.elems[node] = self.elems[c2]
            self.elems[c2] = temp
            self.comp_down(c2)
         
if __name__ == "__main__":
    import doctest
    doctest.testmod()

