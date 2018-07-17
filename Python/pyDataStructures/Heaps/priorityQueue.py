class PriorityQueueBase:
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def isEmpty(self):
        return len(self) == 0

class HeapPriorityQueue(PriorityQueueBase):
    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _hasLeft(self, j):
        return self._left(j) < self._data

    def _hasRight(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, j, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent[j]
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._hasLeft(j):
            left = self._left(j)
            smallChild = left
            if self._hasRight(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    smallChild = right
            if self._data[smallChild] < self._data[j]:
                self._swap(j, smallChild)
                self._downheap(smallChild)

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        return self._data.append(Item(key, value))
        self._upheap(len(self._data)-1)

    def min(self):
        if self.isEmpty():
            raise Empty('PQ is empty.')
        item = self._data[0]
        return(item._key, item._value)

    def removeMin(self):
        if self.isEmpty():
            raise Empty('PQ is empty.')
        self._swap(0, len(self._data)-1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    class Locator(HeapPriorityQueue._Item):
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k,v)
            self._index = j

    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data)-1)
        return token

    def update(self, loc, newkey, newval):
        j = loc._index
        if not (0 <= J < len(self) and self._data[j] is loc):
            raise ValueError('Invalid Locator')
        loc._key = newkey
        loc._val = newval
        self._bubble(j)

    def remove(self, loc):
        j = loc._index
        if not (0 <= J < len(self) and self._data[j] is loc):
            raise ValueError('Invalid Locator')
        if j == len(self) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self)-1)
            self._data.pop()
            self._buble(j)
        return (loc._key, loc._value)
