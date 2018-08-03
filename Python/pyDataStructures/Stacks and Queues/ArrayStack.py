"""
This stack implementation is based from Goodrich, Tammasia, & Goldwasser's
stack implementation in 'Data Structures and Algorithms in Python'
"""

#push - append
#pop/peek [-1]/pop

class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0:

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.isEmpty():
            raise Empty('Stack is Empty')
        return self._data[-1]

    def pop(self):
        if self.isEmpty:
            raise Empty('Stack is Empty')
        else:
            return self._data.pop()
