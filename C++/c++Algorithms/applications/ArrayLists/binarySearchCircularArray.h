//********************************************************************************
// binarySearchCircularArray performs binary search on a sorted vector that has
// been rotated. 
//       ex. [1, 2, 3, 4] -> [4, 1, 2, 3] returns 1 rotation
// Returns the index where the target was found, or -1 if input vector is invalid.

//Algorithm:
        /*
        -create mid
        -check mid
        -check if low < mid
            --true: left-half is sorted
            --false: right-half is sorted
        --if left-half is sorted: is target between low and mid?
            --true: low is mid + 1;
            --false: high = mid - 1
        */
//********************************************************************************

#include <iostream>
#include <vector>
using namespace std;

int binarySearchCircularArray(vector<int> L, int target)
{
    int low = 0;
    int high = L.size() - 1;
    int mid;
    bool sortedLeft;

    while(low <= high)
    {
        mid = (low + high) / 2;
        if(L[mid] == target)
            return mid;
        else if (L[low] < L[mid])
            sortedLeft = 1;
        else
            sortedLeft = 0;

        if(sortedLeft && L[low] <= target && target <= L[mid])
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}

int main()
{
    vector<int> testVec = {5,6,7,8,9,10,11,12,1,2,3,4};
    cout << binarySearchCircularArray(testVec, 13);
}