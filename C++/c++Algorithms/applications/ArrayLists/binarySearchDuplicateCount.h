// Code written (with modifications) from myCodeSchool's tutorial (link below)
// https://www.youtube.com/watch?v=pLT_9jwaPLs


//******************************************************************************
// binarySearchDuplicateCount (bSDC) can be used to find the first and last
// instances of a duplicate value in a SORTED vector. If searchFirst parameter
// is true, will return first instance of target. If false, will return the last.

// Main Function below shows how bSDC can be used to find number of duplicates
// present.
//******************************************************************************

#include <iostream>
#include <vector>

using namespace std;

template <class T>
const int binarySearchDuplicateCount(vector<T> searchVec, T target, bool searchFirst)
{  
    int low = 0;
    int high = searchVec.size() - 1;
    int result = -1;
    int mid;

    while(low <= high)
    {
        mid = (low + high) / 2;

        if(searchVec[mid] == target)
        {
            result = mid;
            if(searchFirst)
                high = mid - 1;
            else
                low = mid + 1;
        }
        else if(searchVec[mid] > target)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return result;
}

int main()
{
    vector<int> A = {1, 1, 3, 3, 5, 5, 5, 5, 5, 9 ,9, 11};
    int target = 1;

    int firstIndex = binarySearchDuplicateCount(A, target, true);
    if(firstIndex == -1)
        cout << "Target \"" << target <<
                "\" is not in the array." << endl;
    else
    {
        int lastIndex = binarySearchDuplicateCount(A, target, false);
        cout << "Target \"" << target << "\" appears " <<
             (lastIndex - firstIndex + 1) << " times." << endl;
    }
}