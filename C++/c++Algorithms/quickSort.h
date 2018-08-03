// Code transcribed (with modifications) from mycodeschool's quickSort algorithm tutorial
// https://www.youtube.com/watch?v=COk73cpQbFQ

#ifndef QUICKSORT_H
#define QUICKSORT_H

#include <iostream>
#include <algorithm>
using namespace std;

template <class T>
int Partition(T* A, int start, int last)
{
    int pivot = A[last];
    int pIndex = start;

    for(int j = start; j < last; j++)
    {
        if(A[j] <= pivot)
        {
            swap(A[j], A[pIndex]);
            pIndex++;
        }
    }
    swap(A[pIndex], A[last]);
    return pIndex;
}

template <class T>
void quickSort(T* A, int start, int last)
{
    if(start < last)
    {
        int pIndex = Partition(A, start, last);
        quickSort(A, start, pIndex-1);
        quickSort(A, pIndex+1, last);
    }
}

#endif // QUICKSORT_H

