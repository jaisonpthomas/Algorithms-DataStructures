#ifndef STACK_TEMPLATE_STATIC_H
#define STACK_TEMPLATE_STATIC_H

#include <iostream>

using namespace std;

template <class T>
class StaticStack
{
    private:
        T* stackArray;
        int stackSize;
        int top;

    public:
        //Constructor
        StaticStack(int);
        //Copy Constructor
        StaticStack(const StaticStack&);

        //Destructor
        ~StaticStack()
        { if(stackSize>0) delete [] stackArray;}

        //MemberFunctions
        void push(T);
        void pop(T&);
        bool isFull()
            { if(top == stackSize - 1) return true;
              else return false; }
        bool isEmpty()
            { if(top == -1) return true;
              else return false; }
        void display() const;
};

//********************************************************
// Constructor
//********************************************************
template <class T>
StaticStack<T>::StaticStack(int size)
{
    stackArray = new T[size];
    stackSize = size;
    top = -1;
    //DEBUG
    //for(int i = 0; i < size; i++)
    //    stackArray[i] = 0;
}

//********************************************************
// Copy Constructor
//********************************************************
template <class T>
StaticStack<T>::StaticStack(const StaticStack& obj)
{
    if(obj.stackSize>0)
        stackArray = new T[obj.stackSize];
    else
        stackArray = nullptr;

    stackSize = obj.stackSize;
    for(int count = 0; count < stackSize; count++)
        stackArray[count] = obj.stackArray[count];

    top = obj.top;
}

//********************************************************
// push adds the argument onto the stack
//********************************************************
template <class T>
void StaticStack<T>::push(T item)
{
    if(isFull())
        cout << "Stack is full. Cannot push " << item << " onto the stack.\n";
    else
        stackArray[++top] = item;

}
//********************************************************
// pop removes the top value from the stack and stores
// it in the variable reference passed as argument
//********************************************************
template <class T>
void StaticStack<T>::pop(T& popHolder)
{
    if(isEmpty())
        cout << "The stack is empty. Cannot pop\n";
    else
        popHolder = stackArray[top--];
}
//********************************************************
// display prints all items in the stack, from top (last in)
// to bottom (first in)
//********************************************************
template <class T>
void StaticStack<T>::display const()
{
    cout << "Stack Items from Top to Bottom:\n";
    for(int i = top; i > -1; i--)
        cout << stackArray[i] << endl;
}

#endif
