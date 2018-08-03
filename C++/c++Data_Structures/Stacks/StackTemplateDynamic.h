//Implementation modeled (with modifications) from
// Tony Gaddis' "C++: From Control Structures through Early Objects 8e"

#ifndef STACK_TEMPLATE_DYNAMIC_H
#define STACK_TEMPLATE_DYNAMIC_H

#include <iostream>
#include <string>
using namespace std;

template <class T>
class DynamicStack
{
    private:
        struct stackNode
        {
            T value;
            stackNode* next;
        };
        stackNode* top;

    public:
        //Constructor
        DynamicStack()
        { top = nullptr; }
        //Destructor
        ~DynamicStack();

        //Stack Functions
        void push(T);
        void pop (T&);
        bool isEmpty()          //if Stack is empty, returns true
        { return (!top); }
        void display() const;

};

//********************************************************
// Destructor
//********************************************************
template <class T>
DynamicStack<T>::~DynamicStack()
{
    stackNode *currNode, *nextNode;
    currNode = top;
    while(currNode)
    {
        nextNode = currNode->next;
        delete currNode;
        currNode = nextNode;
    }
}
//********************************************************
// push will add a new item onto the stack
//********************************************************
template <class T>
void DynamicStack<T>::push(T item)
{
    StackNode* newNode = new StackNode;
    newNode->value = newVal;
    newNode->next = top;
    top = newNode;

}
//********************************************************
// pop will remove the top item from the stack
// and copy it to the variable passed as an argument
//********************************************************
template <class T>
void DynamicStack<T>::pop(T& popVariable)
{
    stackNode* temp = nullptr;

    if(isEmpty())
        cout << "The stack is empty - cannot pop.\n";
        //throw "Error: You are trying to pop from an empty stack.\n";
    else
    {
        holderVariable = top->value;
        temp = top;
        top = top->next;
        delete temp;
    }
}
//********************************************************
// displayStack will print all items in the stack from top
// to bottom
//********************************************************
template <class T>
void DynamicStack<T>::display() const
{
    auto currNode = top;
    cout << "Stack Items from Top to Bottom:" << endl;
    while(currNode)
    {
        cout << currNode->value << endl;
        currNode = currNode->next;
    }
}

#endif
