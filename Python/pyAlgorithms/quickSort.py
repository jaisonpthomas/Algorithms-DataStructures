import random

def quickSort(arr):

    def partition(arr, start, last):
        pivot = arr[last]
        pIndex = start

        for j in range(start, last):
            if arr[j] <= pivot:
                arr[j], arr[pIndex] = arr[pIndex], arr[j]
                pIndex += 1
        arr[pIndex], arr[last] = arr[last], arr[pIndex]
        
        return pIndex

    def quickSortHelper(arr, start, last):
        if start < last:
            pIndex = partition(arr, start, last)
            quickSortHelper(arr, start, pIndex-1)
            quickSortHelper(arr, pIndex+1, last)

    random.shuffle(arr)
    quickSortHelper(arr, 0, len(arr)-1)

testList = [1,5,4,2,3, 0, -3, -10, 7]
quickSort(testList)