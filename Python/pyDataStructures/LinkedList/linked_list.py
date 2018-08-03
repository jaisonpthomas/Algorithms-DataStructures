class ListNode:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __len__(self):
		return self.size

	def add(self, newData):
		newNode = ListNode(newData):
		self.tail.next = newNode
		self.tail = self.tail.next
		self.size += 1

	def remove(self, removeData):
		currNode = self.head
		prevNode = None

		while currNode and currNode != removeData:
			prevNode = currNode
			currNode = currNode.next

		if currNode is None:
			return False
		elif currNode is self.head:
			self.head = self.head.next
		else:
			prevNode.next = currNode.next

		self.size -= 1
		return True

	def find(self, findData):
		currNode = self.head

		while currNode and currNode != findData:
			currNode = currNode.next

		if currNode:
			return True

		else:
			return False