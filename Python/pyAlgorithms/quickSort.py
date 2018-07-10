def partition(A, start, last):
    pivot = A[last];
    pIndex = start;

    for j in range(start, last):
        if A[j] <= pivot:
            A[j], A[pIndex] = A[pIndex], A[j]
            pIndex += 1
    A[pIndex], A[last] = A[last], A[pIndex]
    
    return pIndex

def quickSort(A, start, last):
    if start < last:
        pIndex = partition(A, start, last)
        quickSort(A, start, pIndex-1)
        quickSort(A, pIndex+1, last)


alpha = [1,5,4,2,3, 0, -3, -10, 7]
quickSort(alpha, 0, len(alpha)-1)