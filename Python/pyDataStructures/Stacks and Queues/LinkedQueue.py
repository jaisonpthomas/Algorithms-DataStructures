"""
This queue implementation is based from Goodrich, Tammasia, & Goldwasser's
queue implementation in 'Data Structures and Algorithms in Python'
"""

class LinkedQueue:
    class _Node:
        __slots__ = '_value', '_next'
        def __init__(self, value, next = None):
            self._value = value
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def first(self):
        if not self.isEmpty():
            return self._head._value

    def dequeue(self):
        if not self.isEmpty():
            deqVal = self._head._value
            self._head = self._head._next
            self._size -= 1
            if self.isEmpty():
                self._tail = None
            return answer

    def enqueue(self, newVal):
        newNode = self._Node(newVal)
        if self.isEmpty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1