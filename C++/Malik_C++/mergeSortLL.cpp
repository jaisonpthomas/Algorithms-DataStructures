template <class Type>
void unorderedLinkedList<Type>::
divideList(nodeType<Type>* first1, nodeType<Type>* &first2)
{
    nodeType<Type>* middle;
    nodeType<Type>* current;
    if (first1 == NULL)                 //list is empty
        first2 = NULL;
    else if (first1->link == NULL)      //list has only one node
        first2 = NULL;
    else
    {
        middle = first1;
        current = first1->link;
        if (current != NULL)            //list has more than two nodes
            current = current->link;
        while (current != NULL)
        {
            middle = middle->link;
            current = current->link;
                if (current != NULL)
                    current = current->link;
        } //end while
        first2 = middle->link;          //first2 points to the first
                                        //node of the second sublist
        middle->link = NULL;            //set the link of the last node
                                        //of the first sublist to NULL
    } //end else
} //end divideList

template <class Type>
nodeType<Type>* unorderedLinkedList<Type>::
mergeList(nodeType<Type>* first1, nodeType<Type>* first2)
{
    nodeType<Type> *lastSmall;          //pointer to the last node of
                                        //the merged list
    nodeType<Type> *newHead;            //pointer to the merged list
    if (first1 == NULL)                 //the first sublist is empty
        return first2;
    else if (first2 == NULL)            //the second sublist is empty
        return first1;
    else
    {
        if (first1->info < first2->info) //compare the first nodes
        {
            newHead = first1;
            first1 = first1->link;
            lastSmall = newHead;
        }
        else
        {
            newHead = first2;
            first2 = first2->link;
            lastSmall = newHead;
        }
        while (first1 != NULL && first2 != NULL)
        {
            if (first1->info < first2->info)
            {
                lastSmall->link = first1;
                lastSmall = lastSmall->link;
                first1 = first1->link;
            }
            else
            {
                lastSmall->link = first2;
                lastSmall = lastSmall->link;
                first2 = first2->link;
            }
        } //end while
        if (first1 == NULL)                 //first sublist is exhausted first
            lastSmall->link = first2;
        else                                //second sublist is exhausted first
            lastSmall->link = first1;
        return newHead;
    }
}//end mergeList

template <class Type>
void unorderedLinkedList<Type>::recMergeSort(nodeType<Type>* &head)
{
    nodeType<Type> *otherHead;

    if (head != NULL) //if the list is not empty
        if (head->link != NULL) //if the list has more than one node
        {
        divideList(head, otherHead);
        recMergeSort(head);
        recMergeSort(otherHead);
        head = mergeList(head, otherHead);
        }
} //end recMergeSort

template<class Type>
void unorderedLinkedList<Type>::mergeSort()
{
    recMergeSort(first);
    if (first == NULL)
        last = NULL;
    else
    {
        last = first;
        while (last->link != NULL)
        last = last->link;
    }
} //end mergeSort