"""
This queue implementation is based from Goodrich, Tammasia, & Goldwasser's
queue implementation in 'Data Structures and Algorithms in Python'
"""

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data  = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def first(self):
        if self.isEmpty():
            raise Empty('Queue is Empty')
        else:
            return self._data[self._front]

    def dequeue(self):
        if self.isEmpty():
            raise Empty('Queue is Empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self):
        if self._size == len(self._data)
           s gelf._resize(2 * len(self._data))
        avail = (self._front + self._size) & len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0