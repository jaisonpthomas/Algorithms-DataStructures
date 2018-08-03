class MaxHeap:
    def __init__(self, items = []):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self._floatUp(len(self.heap)-1)

    def push(self, item):
        self.heap.append(item)
        self.heap._floatUp(len(self.heap)-1)

    def peek(self):
        if len(self.heap) >=1:
            return self.heap[1]
        else:
            print("Cannot peek - Heap is empty - returning False")
            return False

    def pop(self):
        if len(self.heap) > 1:
            self._swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self._bubbleDown(1)
            return max
        else:
            print("Cannot pop - Heap is empty - returning False")
            return False

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _floatUp(self, index):
        if index <= 1:
            return

        parent = index // 2
        if self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            self._floatUp(parent)

    def _bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[left] > self.heap[largest]:
            largest = left
        if len(self.heap) > right and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self._swap(index, largest)
            self._bubbleDown(largest)