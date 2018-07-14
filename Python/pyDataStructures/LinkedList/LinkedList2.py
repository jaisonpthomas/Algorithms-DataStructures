class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubllyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def getLength(self):
        return self.length

    def insert(self, insertVal):
        newNode = ListNode(insertVal)

        if self.head is None:
            self.head = newNode
            self.length += 1
        else:
            currNode = self.head
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = newNode
            newNode.prev = currNode
            self.length += 1

    def insertList(self, insertionList):
        for item in insertionList:
            self.insert(item)

    def delete(self, removeVal):
        if self.head is None:
            print("Cannot delete - list is empty")
            return
        if self.head.data == removeVal:
            self.head = self.head.next
            self.length -= 1
        else:
            currNode = self.head
            prev = None
            while(currNode and currNode.value != removeVal):
                prev = currNode
                currNode = currNode.next
            if(currNode and currNode.data == removeVal):
                prev.next = currNode.next
                currNode.next.prev = prev
                self.length -= 1

    def search(self, searchVal):
        currNode = self.head
        while(currNode and currNode != searchVal):
            currNode = currNode.next
        if(currNode == searchVal):
            return True
        else:
            return False

    def __str__(self):
        output = ""
        currNode = self.head
        while currNode:
            output += str(currNode.data)
            output += " -> "
            currNode = currNode.next
        output += "NULL"
        return output

    def sort(self):


