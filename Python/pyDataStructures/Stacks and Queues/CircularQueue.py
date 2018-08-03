"""
This queue implementation is based from Goodrich, Tammasia, & Goldwasser's
queue implementation in 'Data Structures and Algorithms in Python'
"""

class CircularQueue:
    class _Node:
        __slots__ = '_value', '_next'

        def __init__(self, value, next = None):
            self._value = value
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def first(self):
        if not self.isEmpty():
            head = self._tail._next
            return head._value

    def dequeue(self):
        if not self.isEmpty():
            oldHead = self._tail._next
            if self._size == 1:
                self._tail = None
            else:
                self._tail._next = oldHead._next
            self._size -= 1
            return oldHead._element

    def enqueue(self, e):
        newNode = self._Node(e, None)
        if self.isEmpty():
            newNode.next = newNode
        else:
            newNode.next = self._tail._next
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
            


