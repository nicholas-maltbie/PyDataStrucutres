from HashTable import HashTable
from Node import Node

class Partition:
    """
    
    Contains a definition for a partition (inverted tree).
    
    Contains constant time operations for set union of a partioned (all
    disjoint)group of sets.
    
    """
    
    def __init__(self, size):
        self.table = HashTable()
        
    
    
