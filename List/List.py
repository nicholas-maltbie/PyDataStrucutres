"""
char *ident;                  // In case the list has some identity
   bool startoflist;             // True after "startOfList()" is called
   compareFunc *cmpfunc;         // Compare function
   displayFunc *dispfunc;        // Display function

   // The following support sorting the list
   void splitList(List*);
   bool oneElement();
   static List *merge(List*, List*, int(*)(void*));

 protected:
   Node *tail, *current;         // Tail for the list, current to walk through

 public:
   List(compareFunc*, displayFunc*);
   List();
   void insert(void*);       // Insert an object at the rear of the list
   void insertfront(void*);  // Insert an object at the front of the list
   void *startOfList();      // Sets "current" to reference the list's 2nd
                             // object.  Returns the first list object.
                             // Sets "startoflist" to true.
   bool endOfList();         // Returns true if "current" references 1st
                             // list object and "startoflist" is false
   void *nextObject();       // Returns object referenced by "current" and
                             // changes "current" to reference next list object
   Node *nextNode();         // Same as able except returns a node
   void *peek();             // Returns front list object, list not affected
   void *lookup(void*);      // Returns object "same" as input object
                             // according to the "cmpfunc"
   void *remove();           // Returns front list object and removes it
   void *pop(void*);         // Returns object "same" as input object
                             // according to "cmpfunc" and removes it
   bool isEmpty();           // Returns true iff list holds no objects
   void display();           // Print the list of objects
   int stats();
   static List *mergeSort(List*, int(*)(void*));

"""

class List:
    """
    List class, contains definition for linked list.
    """
    
    empty = None

    def __init__(compare_fn, diaply_fn:
        self.compare_fn = compare_fn
        self.display_fn = display_fn
        


if __name__ == "__main__":
    pass
