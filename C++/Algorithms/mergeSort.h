// Code based on mycodeschool's quickSort algorithm tutorial (with modifications)
// https://gist.github.com/mycodeschool/967802
// Tutorial Video: https://www.youtube.com/watch?v=TzeBrDU-JaY&t=19s

#include <iostream>
using namespace std;

void mergeLists(int *A, int *L, int leftCount, int *R, int rightCount)
{
    int i, j, k;
    i = j = k = 0;

    while(i < leftCount && j < rightCount)
    {
        if(L[i] < R[j])
            A[k++] = L[i++];
        else
            A[k++] = R[j++];
    }

    while(i < leftCount)
        A[k++] = L[i++];

    while(j < rightCount)
        A[k++] = R[j++];
}

void mergeSort(int *A, int n)
{
    int mid, *L, *R;

    if(n < 2)
        return;

    mid = n / 2;

    L = new int[mid * sizeof(A[0])];
    R = new int[(n - mid) * sizeof(A[mid])];

    for(int i = 0; i < mid; i++)
        L[i] = A[i];
    for(int i = mid; i < n; i++)
        R[i-mid] = A[i];                    //Don't forget i-mid to start filling at 0!

    mergeSort(L, mid);
    mergeSort(R, n-mid);
    mergeLists(A, L, mid, R, n-mid);

    delete L;
    delete R;
}

int main() {
    int A[] = {5,3,1,2,4};
    int n = sizeof(A)/sizeof(A[0]);

    mergeSort(A, n);

    for(int i = 0; i < n; i++)
        cout << A[i] << " ";
}
