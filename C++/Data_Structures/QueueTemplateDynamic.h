//Implementation based on Tony Gaddis' "C++: From Control Structures through Objects"
// with modifications

#ifndef DYNAMIC_QUEUE_TEMPLATE_H
#define DYNAMIC_QUEUE_TEMPLATE_H

template <class T>
class DynamicQueue
{
private:
    struct QueueNode
    {
        T value;
        QueueNode* next;
    };
    QueueNode* front;
    QueueNode* back;
    int numItems;
public:
    DynamicQueue();
    ~DynamicQueue();

    void enqueue(T);
    void dequeue(T&);
    bool isEmpty() const;
    void clear();
    void display() const;
};

//*****************************************************
// Constructor creates an empty queue
//*****************************************************
template <class T>
DynamicQueue<T>::DynamicQueue()
{
    front = nullptr;
    back = nullptr;
    numItems = 0;
}
//*****************************************************
// Destructor
//*****************************************************
template <class T>
DynamicQueue<T>::~DynamicQueue()
{
    clear();
}
//*****************************************************
// enqueue inserts value at the rear of the queue
//*****************************************************
template <class T>
void DynamicQueue<T>::enqueue(T item)
{
    QueueNode* newNode = new QueueNode;
    newNode->value = item;
    newNode->next = nullptr;
    if(isEmpty())
    {
        front = newNode;
        back = newNode;
    }
    else
    {
        back->next = newNode;
        back = back->next;
    }
    numItems++;
}

template <class T>
void DynamicQueue<T>::dequeue(T& dequeueHolder)
{
    QueueNode* temp = nullptr;

    if(isEmpty())
    {
        cout << "Cannot dequeue from empty queue";
    }
    else
    {
        dequeueHolder = front->value;
        temp = front;
        front = front->next;
        delete temp;

        numItems--;
    }
}

template <class T>
bool DynamicQueue<T>::isEmpty() const;
{
    if(numItems > 0)
        return false;
    else
        return true;
}

template <class T>
void DynamicQueue<T>::clear()
{
    T temp;        //dummy value to hold dequeues - will be destroyed when function returns

    while(!isEmpty)
        dequeue(temp);
}

template <class T>
void DynamicQueue<T>::display() const;
{
    QueueNode* nodePtr = front;
    while(nodePtr)
    {
        cout << nodePtr->value << endl;
        nodePtr = nodePtr->next;
    }

}

#endif
