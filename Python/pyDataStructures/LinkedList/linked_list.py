class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class Linked_list:
	def __init__(self):
		self.head=node()

	def append(self, data):
		new_node = node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node

	def length(self):
		cur = self.head
		total = 0
		while cur.next != None
			total += 1
			cur = cur.next
		return total

	def display(self):
		elems = []
		cur_node = self.head
		while cur.next != None:
			cur_node = cur.next
			elems.append(cur_node.data)
		print(elems)