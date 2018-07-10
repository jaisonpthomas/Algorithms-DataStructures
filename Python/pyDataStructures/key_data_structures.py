class Vertex:
	def __init__(self, name):
		"""name is a string"""
		self.name = name
		self.neighbors = []

	def add_neighbor(self, neighbor):
		"""neighbor will be the string name for the neighbor object"""
		if neighbor not in self.neighbors:
			self.neighbors.append(neighbor)
			self.neighbors.sort()

class Graph:
	vertices = {}

	def add_vertex(self, vertex):
		"""vertex is the actual vertex object"""
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else: return False

	def add_edge(self, u, v):
		"""u and v will be the string names for the ertices"""
		if u in self.vertices and v in self.vertices:
			self.vertices[u].add_neighbor(v)
			self.vertices[v].add_neighbor(u)

	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + " " + str(self.vertices[key].neighbors))

	def DFS(self):
		visited = []

	def DFSRecur(node, visited)
		for vertex in self.vertices



class MaxHeap:
	def __init__(self, items = []):
		self.heap = [0]
		for item in items:
			self.heap.append(item)
			self.heap.__floatUp(len(self.heap)-1)

	def push(self, item):
		self.heap.append(item)
		self.heap.__floatUp(len(self.heap)-1)

	def peek(self):
		if len(self.heap) >=1:
			return self.heap[1]
		else:
			return False

	def pop(self):
		if len(self.heap) == 2:
			max = self.heap.pop()
		elif len(self.heap > 2):
			self.__swap(1, len(self.heap)-1)
			max = self.heap.pop()
			self.__bubbleDown(1)
		else:
			max = False
		return max

	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):
		parent = index // 2
		if index <= 1: return
		elif self.heap[index] > self.heap[parent]:
			self.__swap(self, index, parent)
			self.__floatUp(parent)

	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 + 1
		largest = index
		if len(self.heap) > left and self.heap[left] > self.heap[largest]:
			largest = left
		if len(self.heap) > right and self.heap[right] > self.heap[largest]:
			largest = right
		if largest != index:
			self.__swap(index, largest)
			self.__bubbleDown(largest)


class linkedListQueue:

	class Node:
		def __init__(self, data, next):
			self.data = data
			self.next = next

	def __init__(self, front=None, back=None):
		self.queue = {'front': front, 'back': back}

	def __str__(self):
		if self.queue['front'] is None and self.queue['back'] is None:
			return "Queue is empty"
		return "Front: " + str(self.queue['front'].data) + " Back: " + str(self.queue['back'].data)

	def enqueue(self, element):
		N = Node(element, None)
		if self.queue['back'] == None:
			self.queue['front'] = N
			self.queue['back'] = N
		else:
			self.queue['back'].next = N
			self.queue['back'] = N

	def dequeue(self):
		if self.queue['front'] != None:
			first = self.queue['front']
			self.queue['front'] = self.queue['front'].next
			return first.data
		else:
			return 'Cannot dequeue from empty queue'
        
	myQueue = linkedListQueue()
	print(myQueue)

	myQueue.enqueue('a')
	myQueue.enqueue('b')
	myQueue.enqueue('c')
	print(myQueue.dequeue())
	print(myQueue.dequeue())

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans