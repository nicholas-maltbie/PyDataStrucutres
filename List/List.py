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
    >>> lst.stats()
    1
    >>> lst.insert(10)
    >>> lst.stats()
    2
    >>> lst.lookup(5)
    True
    >>> lst.remove()
    5
    >>> lst.lookup(5)
    False
    >>> a = List()
    >>> b = List()
    >>> a.insert(5)
    >>> b.insert(10)
    >>> c = List.merge(a, b)
    >>> c
    5 10 
    >>> l1 = List()
    >>> import random
    >>> for i in range(1000):
    ...   l1.insert(random.randrange(10000))
    >>> l1_sorted = List.merge_sort(l1)
    >>> l1_sorted.stats()
    1000
    >>> lst = List()
    >>> lst.insert(100)
    >>> lst.insert(500)
    >>> lst.insert(-10)
    >>> lst.insert(50)
    >>> lst
    100 500 -10 50 
    >>> lst = lst.merge_sort()
    >>> lst
    -10 50 100 500 
    >>> 
    """
    
    default_compare = lambda a, b: -1 if a < b else 1 if a > b else 0
    default_disp = lambda x: str(x)

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
        if self.is_empty():
            return False
        p = self.tail.next
        while p != self.tail:
            if self.compare_fn(p.val, val) == 0:
                return True
            p = p.next
        if self.compare_fn(self.tail.val, val) == 0:
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
            self.tail = empty
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
        if self.tail is empty:
            return
        p = self.tail.next
        while p != self.tail:
            if self.compare_fn(p.next.val, val) == 0:
                obj = p.next.val
                ptr = p.next
                p.next = p.next.next
                return obj
            p = p.next
        if self.compare_fn(self.tail.val, val) == 0:
            obj = self.tail.val
            self.tail = empty
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
    
    def __iter__(self):
        if self.tail is not empty:
            p = self.tail.next
            while p.next != self.tail.next:
                yield p.val
                p = p.next
            yield self.tail.val
            
    def display(self):
        if self.display_fn == None:
            return "No display"
        elif self.tail is empty:
            return "<>"
        else:
            return ", ".join([self.display_fn(val) for val in iter(self)])
    
    def __repr__(self):
        return self.display()
        
    def split_list(self, l1):
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
        l1.insert(val1)
        if flag:
            self.insert(val2)
    
    def __len__(self):
        return self.stats();
    
    def one_element(self):
        if self.tail is empty:
            return True
        if self.tail.next == self.tail:
            return True
        return False
    
    def peek(self):
        if self.tail is empty:
            return empty
        return self.tail.next.val
        
    def stats(self):
        if self.tail is empty:
            return 0
        count = 0
        p = self.tail.next
        while p != self.tail:
            count += 1
            p = p.next
        return count + 1
        
    def merge(q1, q2, eval_fn=default_compare):
        v1 = None
        v2 = None
        v = None
        q = List()
        
        if q1.is_empty():
            return q2
        if q2.is_empty():
            return q1
        
        while not q1.is_empty() and not q2.is_empty():
            v1 = q1.peek()
            v2 = q2.peek()
            if eval_fn(v1, v2) < 0:
                v = q1.remove()
            else:
                v = q2.remove()
            q.insert(v)
            
        while not q1.is_empty():
            q.insert(q1.remove())
        while not q2.is_empty():
            q.insert(q2.remove())
        
        return q
        
    
    def merge_sort(lst, eval_fn=default_compare):
        if lst is empty:
            return lst
        if lst.one_element():
            return lst
        tmp = List()
        lst.split_list(tmp)
        lst = List.merge_sort(lst, eval_fn)
        tmp = List.merge_sort(tmp, eval_fn)
        lst = List.merge(lst, tmp, eval_fn)
        lst.current = lst.tail.next
        lst.startoflist = True
        return lst
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

