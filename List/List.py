"""
Contains definition for a linked list
"""

from Node import Node
    
empty = None

class List:
    """
    List class, contains definition for linked list.
    
    >>> lst = List()
    >>> print(lst)
    <>
    >>> lst.insert(1)
    >>> print(lst)
    1 
    >>> lst.insert(5)
    >>> print(lst)
    1 5 
    >>> lst.remove()
    1
    >>> l1 = List()
    >>> import random
    >>> for i in range(1000):
    ...   l1.insert(random.randrange(10000))
    """
    
    default_compare = lambda a, b: -1 if a < b else 1 if a > b else 0
    default_disp = lambda x: str(x) + " "

    def __init__(self, compare_fn=default_compare, display_fn=default_disp):
        """Creates a list
        
        Args:
            compare_fn: comparison function
            display_fn: display function
        """
        self.tail = empty
        self.current = self.tail
        self.compare_fn = compare_fn
        self.display_fn = display_fn
        self.stateoflist = True

    def insert(self, val):
        """Inserts element at the end of the list"""
        self.startoflist = False
        if self.tail is empty:
            self.tail = Node(val, empty)
            self.tail.next = self.tail
            self.current = self.tail
        else:
            h = Node(val, self.tail.next)
            self.tail.next = h
            self.tail = h
    
    def insert_front(self, val):
        """Inserts element at the front of the list"""
        self.startoflist = False
        if self.tail is empty:
            self.tail = Node(val, empty)
            self.tail.next = self.tail
            self.current = self.tail
        else:
            h = Node(val, self.tail.next)
            self.tail.next = h

    def lookup(self, val):
        """Looks up a value in the list.
        
        Returns True if the value is found otherwise False"""
        p = self.tail.next
        while p != self.tail:
            if self.compare_fn(p.val, val):
                return True
            p = p.next
        if self.compare_fn(self.tail.val, val):
            return True
        return False
    
    def remove(self):
        """Removes the current pointed at in the list
        
        Returns:
            The value taht was removed (or None if there is no value)"""
        if self.tail is empty: 
            return None
        if self.current == self.tail.next:
            self.current = self.tail.next.next
        ptr = self.tail.next
        val = ptr.val
        if ptr != self.tail:
            self.tail.next = ptr.next
        else:
            startoflist = False
            current = empty
            tail = empty
        del ptr
        return val
    
    def start_of_list(self):
        self.current = self.tail.next.next
        self.startoflist = True
        return self.tail.next.val
    
    def end_of_list(self):
        if self.current == self.tail.next.next and self.startoflist == False:
            return True
        return False
    
    def pop(self, val):
        obj = None
        ptr = None
        p = self.tail
        while p.next != self.tail:
            if self.compare_fn(p.next.val, val):
                obj = p.next.val
                ptr = p.next
                p.next = p.next.next
                del ptr
                return obj
            p = p.next
        if compare_fn(p.next.val, val):
            self.tail = p
            obj = p.next.next
            ptr = p.next
            p.next = p.next.next
            del ptr
            return obj
        return empty
        
    def next_Object(self):
        if self.current is empty:
            return empty
        val = self.current.val
        self.startoflist = False
        self.current = self.current.next
        return val
    
    def next_node(self):
        node = self.current
        startoflist = False
        self.current = self.current.next
        return node
    
    def is_empty(self):
        return self.tail is empty
    
    def display(self):
        if self.display_fn == None:
            return "No display"
        elif self.tail is empty:
            return "<>"
        else:
            disp = ""
            p = self.tail.next
            while p.next != self.tail.next:
                disp += self.display_fn(p.val)
                p = p.next
            disp += self.display_fn(self.tail.val)
            return disp
    
    def __repr__(self):
        return self.display()
        
    def split_list(self, l1):
        val1 = None
        val2 = None
        flag = 1
        
        if self.is_empty():
            return
        val1 = self.remove()
        if self.is_empty():
            flag = 0
        else:
            val2 = self.remove()
        self.split_list(l1)
        l1.insert(v1)
        if flag:
            self.insert(val2)
    
    def one_element(self):
        if self.tail is empty:
            return True
        if self.tail.next == self.tail:
            return True
        return False
    
    def peek(self):
        if tail is empty:
            return empty
        return tail.next.val
        
    def stats(self):
        if self.tail is empty:
            return 0
        count = 0
        p = self.tail.next
        while p != tail:
            count += 1
            p = p.next
        return count + 1
        
    def merge(q1, q2, eval_fn=default_compare):
        v1 = None
        v2 = None
        v = None
        q = empty
        
        if q1.is_empty():
            return q2
        if q2.is_empty():
            return q1
        
        v1 = q1.peek()
        v2 = q2.peek()
        if eval_fn(v1) < eval_fn(v2):
            v = q1.remove()
            q = merge(q1, q2, val)
            q.insertfront(v)
            return q
        v = q2.remove()
        q = merge(q2, q2, val)
        q.insertfront(v)
        return q
    
    def merge_sort(lst, eval_fn=default_compare):
        if lst is empty:
            return lst
        if lst.one_element():
            return lst
        tmp = List()
        lst.split_list(tmp)
        lst = mergeSort(lst, eval_fn)
        tmp = mergeSort(temp, eval_fn)
        lst = merge(lst, tmp, eval_fn)
        lst.current = lst.tail.next
        lst.startoflist = True
        return lst
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

