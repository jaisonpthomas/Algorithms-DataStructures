#NOT COMPLETE - IN PROGRESS

def partition(A, startNode, lastNode):
    pivotNode = lastNode
#    for _ in range(last):
#        pivotNode = pivotNode.next                                      #linear time
    pIndexNode = startNode                                               
    jNode = #start

    for j in range(start, last):                                         #linear
        if jNode.data <= pivotNode.data:                                
            jNode.data, pIndexNode.data = pIndexNode.data, jNode.data   
            pIndexNode = pIndexNode.next                                
    pIndexNode.data, pivotNode.data = pivotNode.data, pIndexNode.data 
    
    return pIndexNode

def quickSort(self, start, last):
    if start < last:                                            #<- Need a way to do this
        pIndexNode = partition(start, last)
        quickSort(start, pIndexNode.prev)
        quickSort(pIndexNode.next, last)

def sort(self):
    if myList.length < 2:
        return
    startNode = self.head
    lastNode = startNode
    while lastNode.next:
        lastNode = lastNode.next
    quickSort(startNode, lastNode)



myList.insertList([7,2,1,6,8,5,3,4])
myList.sort()

        #213         4          8576
#21  3                          #5  6   78