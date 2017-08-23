"""

Contains a definition for a hash table

#ifndef _HASHTABLE
#define _HASHTABLE

#include <iostream>
#include "funcs.h"
#include "list.h"
using namespace std;

// Default compare function
class compHashDef : public compareFunc {
   valueFunc *val;

 public:
   compHashDef (valueFunc*);
   int compare (void*, void*);
};

// Default hash function
class hashHashDef : public hashFunc {
   valueFunc *val;
   int number;

 public:
   hashHashDef (valueFunc*, int);
   int hashfn (void*);
};

// Hashtable prototype
class HashTable {
   friend ostream &operator<<(ostream&, HashTable*);
   List **table;
   int size;
   displayFunc *dispfn;
   compareFunc *cmpfn;
   hashFunc *hashfn;

 public:
   HashTable (int, compareFunc*, hashFunc*, displayFunc*);
   HashTable (int, compareFunc*, hashFunc*);
   HashTable (int, valueFunc*);
   HashTable (valueFunc*);
   void *add(void*);
   void *lookup (void*);
   void *pop (void*);
   ~HashTable();
};

ostream &operator<<(ostream&, HashTable*);
#endif

"""

class HashTable:
    

if __name__ == "__main__":
    pass
