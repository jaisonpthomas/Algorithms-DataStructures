// Implementation based on D.S. Malik's "Data Structures Using C++ 2e"
// with modifications

#ifndef BINARY_SEARCH_H
#define BINARY_SEARCH_H

/**
 * binarySearch performs binary search for target in vector searchVector.
 * If found, returns the index where target is located.
 * Otherwise, it returns -1.
 */

template <class T>
int binarySearch(vector<T> searchVector, T target)
{
    int low = 0;
    int high = searchVector.size() - 1;
    int mid;

    while(low <= high)
    {
        mid = (low + high) / 2;

        if(searchVector[mid] == target)
            return mid;
        else if(searchVector[mid] > target)
            high = mid-1;
        else
            low = mid+1;
    }
    return -1;
}

#endif
