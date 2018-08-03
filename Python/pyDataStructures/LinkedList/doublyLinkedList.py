class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def displayNode(self):
        print("<- ", self.data, " -> ", end = " ")

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def insertHead(self, newData):
        newNode = ListNode(newData)
        if self.head is None:           # get pointback to newNode
            self.tail = newNode
        else:
            self.head.prev = newNode

        newNode.next = self.head        # get newNode to point out
        self.head = newNode             # declare head

    def popHead(self):
        if self.isEmpty():
            print("Cannot popHead - list is Empty!")
        else:
            temp = head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
            return temp.data

    def insertTail(self, newData):
        if self.isEmpty():
            self.insertHead(newData)
        else:
            newNode = ListNode(newData)
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = self.tail.next

    def popTail(self):
        if self.isEmpty():
            print("Cannot pop tail - list is empty")
            return

        temp = self.tail
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return temp.data

    def display(self):
        print("NULL ", end = " ")
        currNode = self.head
        while currNode:
            currNode.displayNode()
            currNode = currNode.next
        print(" NULL")

if __name__ == "__main__":
    testList = DoublyLinkedList()
    print("Is List Empty? ", testList.isEmpty())
    
    initList = [5,4,3,2,1]    
    for num in initList:
        testList.insertHead(num)
        
    print("Is List Empty? ", testList.isEmpty())
    testList.display()
    
    appendList = [6,7,8,9]
    for num in appendList:
        testList.insertTail(num)
    testList.display()
    
    poppedHead = testList.popHead()
    poppedTail = testList.popTail()
    print("poppedHead is: ", poppedHead)
    print("poppedTail is: ", poppedTail)
    
    testList.display()
