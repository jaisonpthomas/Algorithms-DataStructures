"""
This stack implementation is based from Goodrich, Tammasia, & Goldwasser's
stack implementation in 'Data Structures and Algorithms in Python'
"""

class LinkedStack:

    class _Node:
        __slots__ = '_value', '_next'

        def __init__(self, value, next = None):
            self._value = value
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if not self.isEmpty():
            return self._head._value

    def pop(self):
        if not self.isEmpty():
            answer = self._head._value
            self._head = self._head._next
            self._size -= 1
            return answer