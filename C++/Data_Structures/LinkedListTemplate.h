//Implementation based on Tony Gaddis' "C++: From Control Structures through Objects"
// with modifications

#ifndef LINKED_LIST_TEMPLATE_H
#define LINKED_LIST_TEMPLATE_H

//*****************************************************
// The ListNode class creates a type used to
// store a node of the linked list.
//*****************************************************

template <class T>
class ListNode
{
    public:
        //Member Variables
        T value;
        ListNode<T> *next;

        //Constructor
        ListNode(T nodeValue)
        {
            value = nodeValue;
            next = nullptr;
        }
};


//*****************************************************
// Linked List Class
//*****************************************************

template <class T>
class LinkedList
{
    private:
        ListNode<T>* head;

    public:
        LinkedList()
        { head = nullptr; }

        ~LinkedList();

        void appendNode(T);
        void insertNode(T);
        void deleteNode(T);
        void displayList() const;
};

//*****************************************************
// Destructor
//*****************************************************
LinkedList<T>::~LinkedList()
{
    ListNode<T>* currNode;
    ListNode<T>* nextNode;

    currNode = head;

    while(currNode)
    {
        nextNode = currNode->next;
        delete currNode;
        currNode = newNode;
    }
}

//*****************************************************
// appendNode appends a node TO THE END of the list,
// containing the value passed into newValue
//*****************************************************
template <class T>
void LinkedList<T>::appendNode(T newValue)
{
    ListNode<T>* newNode;
    ListNode<T>* currNode;

    newNode = new ListNode<T>(newValue);

    if(!head)
        head = newNode;
    else
    {
        currNode = head;
        while(currNode->next)
            currNode = currNode->next;
        currNode->next = newNode;
    }
}
//*****************************************************
// insertNode insets a node with a given value into
// appropriate spot into the sorted linked list
//*****************************************************
template <class T>
void LinkedList<T>::insertNode(T newValue)
{
    ListNode<T>* newNode;
    ListNode<T>* currNode;
    ListNode<T>* prevNode;

    prevNode = nullptr;
    newNode = new ListNode<T>(newValue);

    if(!head)
    {
        head = newNode;
    }
    else
    {
        currNode = head;
        while(currNode && currNode->value < newValue)
        {
            prevNode = currNode;
            currNode = currNode->next;
        }
        if(prevNode == nullptr)
        {
            head = newNode;
            head->next = currNode;
        }
        else
        {
            prevNode->next = newNode;
            newNode->next = currNode;
        }
    }
}
//*****************************************************
// deleteNode searches for a node with the passed value.
// if found, will delete node from list and memory.
//*****************************************************
template <class T>
void LinkedList<T>::deleteNode(T searchValue)
{
    ListNode<T>* currNode;
    ListNode<T>* prevNode;

    if(!head)
        cout << "Cannot run deleteNode - list is empty";
        return;
    if(head->value == searchValue)
    {
        currNode = head->next;
        delete head;
        head = currNode;
    }
    else
    {
        currNode = head;
        while(currNode && currNode->value != searchValue)
        {
            prevNode = currNode;
            currNode = currNode->next;
        }
        if(currNode)
        {
            prevNode->next = currNode->next;
            delete currNode;
        }
    }
}
//*****************************************************
// displayList shows the value stored in each node of
// the linked list
//*****************************************************
void LinkedList<T>::displayList() const
{
    ListNode<T>* currNode;
    currNode = head;

    while(currNode)
    {
        cout << currNode->value << endl;
        currNode = currNode->next;
    }
}

#endif
