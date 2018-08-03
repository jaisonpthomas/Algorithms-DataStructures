"""
This is running slowly on leetcode currently. Review/upate.
"""

import random

def quickSelectKthVal(arr, k, smallest=True):
    
    def partition(arr, start, last, k):
        if start == last:
            return arr[start]        
        pivot = arr[last]
        pIndex = start

        for j in range(start, last):
            if arr[j] <= pivot:
                arr[j], arr[pIndex] = arr[pIndex], arr[j]
                pIndex += 1
        arr[pIndex], arr[last] = arr[last], arr[pIndex]         

        if k == pIndex:
            return arr[pIndex]
        elif k < pIndex:
            return partition(arr, start, pIndex-1, k)
        else:
            return partition(arr, pIndex+1, last, k)

    if smallest:
        return partition(arr, 0, len(arr)-1, k-1)
    else:
        return partition(arr, 0, len(arr)-1, len(arr)-k)

    random.shuffle(arr)
    return quickSelectKthVal(arr, k, smallest=False)


alpha = [3,2,3,1,2,4,5,5,6]
alpha.sort()
a = [3,2,3,1,2,4,5,5,6]
k = 6
result = quickSelectKthVal(a, k)

"""
print("SMALLEST VALUES")
for i in range(1,len(a)+1):
    print(i, "smallest value is: ", quickSelectKthVal(a, i, smallest=True))
    
print()
print()

print("LARGEST VALUES")
for i in range(1,len(a)+1):
    print(i, "smallest value is: ", quickSelectKthVal(a, i, smallest=False))
"""   
