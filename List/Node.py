class Node:
    """
    Contains a definition for a node
    
    Attributes:
        val: value held in the node
        next: next node in the sequence
        parent: parent node for inverted trees
        size: size of subtree for inverted trees
    """
    
    def __init__(self, val, next=None, parent=None, size=1):
        """
        Create a new node with a value ans possibly a next node
        
        Args:
            val: value in the node
            next: next node in the list
            parent: support inverted trees
            size: support inverted trees (nodes in subtree)
        """
        self.val = val
        self.next = next
        self.parent = parent
        self.size = size
    
    def identify(self):
        if (self == self.parent):
            return self
        self.parent = self.parent.identify()
        return self.parent

