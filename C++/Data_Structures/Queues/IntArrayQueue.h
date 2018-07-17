//Implementation based on Tony Gaddis' "C++: From Control Structures through Objects"
// with modifications

#ifndef INTARRAYQUEUE_H
#define INTARRAYQUEUE_H

#include <iostream>
using namespace std;

class IntArrayQueue
{
private:
    int* queueArray;
    int queueSize;
    int front;
    int rear;
    int numItems;

public:
    //Constructors
    IntArrayQueue(int)
    IntArrayQueue(const IntArrayQueue&)
`
    ~IntArrayQueue();

    void enqueue(int);
    void dequeue(int&);
    bool isEmpty() const;
    bool isFull() const;
    void clear;
};

IntArrayQueue::IntArrayQueue(int s)
{
    queueArray = new int[s];
    queueSize = s;
    front = -1;
    rear = -1;
    numItems = 0;
}

IntArrayQueue::IntArrayQueue(const IntArrayQueue& obj)
{
    queueArray = new int[obj.queueSize];

    queueSize = obj.queueSize;
    front = obj.front;
    rear = obj.rear;
    numItems = obj.numItems

    for(int i = 0; i < obj.queueSize; i++)
        queueArray[i] = obj.queueArray[i];
}

IntArrayQueue::~IntArrayQueue()
{
    delete [] queueArray;
}

void IntArrayQueue::enqueue(int num)
{
    if(isFull())
        cout << "Cannot enqueue - the queue is full." << endl;
    else
    {
        rear = (rear + 1) % queueSize;
        queueArray[rear] = num;
        numItems++;
    }
}

void IntArrayQueue::dequeue(int& num)
{
    if(isEmpty())
        cout << "Cannot dequeue - the queue is empty." << endl;
    else
    {
        front = (front + 1) % queueSize;
        num = queueArray[front];
        numItems--;
    }
}

void IntArrayQueue::isEmpty()
{
    if(numItems)
        return false
    else
        return true
}

void IntArrayQueue::isFull()
{
    if numItems < queueSize:
        return false
    else
        return true
}

void IntArrayQueue::clear()
{
    front = queueSize - 1
    rear = queueSize - 1
    numItems = 0
}

#endif