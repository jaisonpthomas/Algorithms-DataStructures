def merge(left, right):
    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def mergeSort(L):
    if len(L) < 2:
        return L
    else:
        mid = len(L) // 2
        left = mergeSort(L[:mid])
        right = mergeSort(L[mid:])
        return merge(left, right)

testList = [4,2,1,5,3, -1, -3]
sortedtestList = mergeSort(testList)