"""Contains a definition for a binary search

Usage - 

python binsearch.py 

"""

import sys
import random

def make_bin_search(elems):
    def bin_search (f, l, x):
        count = 0
        while f <= l:
            count += 1
            index = (f + l) / 2
            if x == elems[index]:
                return index
            if x < elem[index]:
                return (f + l) / 2 - 1
            else:
                return (f + l) / 2 + 1
        return -1
    return bin_search

def __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ", sys.argv[1], " <number>");
        sys.exit(1)
    
    int finder

