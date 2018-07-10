"""
 * linearSearch performs linear search for searchVal in a vector searchList.
 * If found, returns the index where searchVal is located.
 * Otherwise, it returns -1.
"""

def linearSearch(searchVec, target):
    for i in range(len(searchVec - 1)):
        if searchVec[i] == target:
            return i
    return -1