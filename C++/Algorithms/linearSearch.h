// Implementation based on D.S. Malik's "Data Structures Using C++ 2e"
// with modifications

#ifndef LINEAR_SEARCH_H
#define LINEAR_SEARCH_H

#include <vector>
#include <string>

using namespace std;

/**
 * linearSearch performs linear search for searchVal in a vector searchList.
 * If found, returns the index where searchVal is located.
 * Otherwise, it returns -1.
 */

<template <class T>
int linearSearch(vector<T> searchList, T searchVal)
{
    int loc;

    for(loc = 0; loc < searchList.size(); loc++)
    {
        if(searchList[loc] == searchVal)
            return loc;
    }
    return -1;
}

#endif // LINEAR_SEARCH_H
