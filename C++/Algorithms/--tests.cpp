#include <iostream>
#include "linearSearch.h"
#include "binarySearch.h"
#include "quickSort.h"
#include <vector>
#include <string>

using namespace std;

int linearSearchTest()
{
    cout << "\n";

    string searchString = "theta";
    vector<string> stringVector = {"alpha", "beta", "gamma"};
    int stringIndex = linearSearch(stringVector, searchString);
    cout << "stringIndex equals: " << stringIndex << endl;

    vector<int> doubleVec = {5,6,7,8};
    int negDoubleIndex = linearSearch(doubleVec, 9);
    cout << "negDoubleIndex equals: " << negDoubleIndex << endl;

    int posDoubleIndex = linearSearch(doubleVec, 5);
    cout << "posDoubleIndex equals: " << posDoubleIndex << endl;
}

int binarySearchTest()
{
    cout << "\n";

    vector<int> intVec = {5,6,7,8,9};

    int posIndex = binarySearch(intVec, 7);
    cout << "BinarySearch posIndex equals: " << posIndex << endl;

    int negIndex = binarySearch(intVec, 12);
    cout << "BinarySearch negIndex equals: " << negIndex << endl;
}

int quickSortTest()
{
    cout << "\n";

    char charTest[] = {'c', 'a', 'b', 'e', 'd'};
    int charTestSize = sizeof(charTest)/sizeof(charTest[0]);
    //int A[] = {7,2,1,6,8,5,3,4};
    quickSort(charTest, 0, charTestSize - 1);

    cout << "QuickSorted Character Array:\n";
    for(int i =0; i < charTestSize; i++)
        cout << charTest[i] << " ";
    cout << endl << endl;

    int intTest[] = {7,2,1,6,8,5,3,4};
    int intTestSize = sizeof(intTest)/sizeof(intTest[0]);
        quickSort(intTest, 0, intTestSize - 1);

    cout << "QuickSorted Integer Array:\n";
    for(int i =0; i < intTestSize; i++)
        cout << intTest[i] << " ";
    cout << endl << endl;
}

int main()
{
    linearSearchTest();
    binarySearchTest();
    quickSortTest();
}
