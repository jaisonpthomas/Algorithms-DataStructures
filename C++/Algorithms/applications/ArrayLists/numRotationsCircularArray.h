// Code written (with modifications) from myCodeSchool's tutorial (link below)
// https://www.youtube.com/watch?v=pLT_9jwaPLs

//NOTES

//Like all binarySearch:
    //set a low and high at the ends
    //set mid
        //find something about one side that you know you can throw out


//******************************************************************************
// findRotationCount can be used with a sorted vector that has been
// rotated. It will tell you how many rotations occurred.
//          ex. [1, 2, 3, 4] -> [4, 1, 2, 3] returns 1 rotation
// Returns 0 if already sorted, returns -1 if input vector is invalid.
//******************************************************************************
template <class T>
int findRotationCount(vector<T> A)
{
    int N = A.size();
    int low = 0;
    int high = N - 1;

    while(low <= high)
    {
        //Case 1 - If it's already sorted, the minimum is at zero (zero rotations).
        if(A[low] <= A[high])       
            return low;

        int mid = (low + high) / 2;
        int next = (mid + 1) % N;                   //get the 2 elements before and after mid         
        int prev = (mid - 1 + N) % N;

        //Case 2 - if mid is greater than next and prev, it's the minimum
        if(A[mid] <= A[next] && A[mid] <= A[prev])
            return mid;

        //Case 3 - Right half is sorted (go to left - min will be in unsorted half)
        else if(A[mid] <= A[high])
            high = mid - 1;

        //Case 4- Left half sorted (throw out left - go to right)
        else
            low = mid + 1;
    }
    return -1;
}

int main()
{
    vector<int> testVec = {5, 1, 2, 3, 4};
    int rotCount = findRotationCount(testVec);
    cout << rotCount << endl;
}