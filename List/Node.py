class Node:
    """
    Contains a definition for a node
    """
    
    def __init__(val, next=None, parent=None, size=-1):
        """
        Create a new node with a value ans possibly a next node
        
        Args - 
            val     : value in the node
            next    : next node in the list
            parent  : support inverted trees
            size    : support inverted trees (nodes in subtree)
        """
        self.val = val
        self.next = next
        
    def get_val(self):
        return self.val
    
    def identify(self):
        if (self == self.parent):
            return self
        self.parent = self.parent.identify()
        return self.parent

