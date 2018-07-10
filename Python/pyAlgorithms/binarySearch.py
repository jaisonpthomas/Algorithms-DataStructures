"""
 * binarySearch performs binary search for target in vector searchVector.
 * If found, returns the index where target is located.
 * Otherwise, it returns -1.
"""

def binarySearch(searchList, target):
    low = 0
    high = len(searchList) - 1

    while low <= high:
        mid = (low + high) // 2
        if searchList[mid] == target:
            return mid
        elif searchList[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1