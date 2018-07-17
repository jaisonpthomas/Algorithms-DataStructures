"""
This graph implementation is based (with modifications/bug-fixes)
from Goodrich, Tammasia, & Goldwasser's graph implementation in
'Data Structures and Algorithms in Python'
"""

class Vertex:
    __slots__ = '_element'

    def __init__(self, x):
        self._element = x

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))

    def __str__(self):
        return str(self._element)

class Edge:
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        return (self._origin, self._destination)

    def opposite(self, v):
        if v is self._origin:
            return self._destination
        else:
            return self._origin

    def element(self):
        return self._element

    def __hash__(self):
        return hash( (self._origin, self._destination) )

    def __str__(self):
        return str(self._origin) + " -> " + str(self._destination)

class Graph:
    def __init__(self, directed = False):
        self._outgoing = {}
        if directed:
            self._incoming = {}
        else:
            self._incoming = self._outgoing

    def __str__(self):
        output = ""
        for vertex in self._outgoing:
            output += str(vertex) + "->  ["
            for vertex in self._outgoing[vertex]:
                output += (str(vertex) + ", ")
            output = output[:-2]
            if output[-1] != " ":
                output += "]"
            output += "\n"
        return output

    def isDirected(self):
        return self._incoming is not self._outgoing

    def vertexCount(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edgeCount(self):
        total = 0
        for v in self._outgoing:
            total += len(self._outgoing[v])
        if self.isDirected():
            return total
        else:
            return total // 2

    def edges(self):
        result = set()
        for secondaryMap in self._outgoing.values():
            result.update(secondaryMap.values())
        return result

    def getEdge(self, u, v):
        return self._outgoing[u][v]

    def degree(self, v, outgoing = True):
        if outgoing:
            return len(self._outgoing[v])
        else:
            return len(self._incoming[v])

    def incidentEdges(self, v, outgoing = True):
        if outgoing:
            adj = self._outgoing
        else:
            adj = self._incoming
        for edge in adj[v].values():
            yield edge

    def insertVertex(self, x=None):
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.isDirected:
            self._incoming[v] = {}
        return v

    def insertEdge(self, u, v, x=None):
        e = Edge(u,v,x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

##graph traversal functions

def DFS(g, u, discovered):
    for e in g.incidentEdges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)

    """

    * Implementation that doesn't require client to provide initial dict.
    * Will return the completed DFS dictionary.


        def DFS(g, u):
            def DFSHelper(g, u, discovered):
                for e in g.incidentEdges(u):
                    v = e.opposite(u)
                    if v not in discovered:
                        discovered[v] = e
                        DFSHelper(g, v, discovered)
            discovered = {u: None}
            DFSHelper(g, u, discovered)
            return discovered
    """

def BFS(g, s, discovered):
    queue = [s]
    while len(queue):
        u = queue.pop(0)
        for e in g.incidentEdges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                queue.append(v)

def constructPath(u, v, discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path

def topologicalSort(g):
    topo = []
    readyStack = []
    inCount = {}

    for u in g.vertices():
        inCount[u] = g.degree(u, False)
        if inCount[u] == 0:
            readyStack.append(u)
    while len(ready):
        u = readyStack.pop()
        topo.append(u)
        for e in g.incidentEdges(u):
            v = e.opposite(u)
            inCount[v] -= 1
            if inCount[v] == 0:
                readyStack.append(v)

    return topo

def dijkstra(g, src):

    d = {}
    cloud = {}
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}

    for v in gvertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')
        pqlocator[v] = pq.add(d[v],v)

    while not pq.isEmpty():
        key, u = pq.removeMin()
        cloud[u] = key
        del pqlocator[u]

        for e in g.incidientEdges(u):
            v = e.opposite(u)
            if v not in cloud:
                wgt = e.element()
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt
                    pq.update(pqlocator[v], d[v], v)

    return cloud

def shortestPathTree(g, src, d):
    tree = {}
    for vertex in d:
        if vertex is not src:
            for e in g.incidientEdges(vertex, False):
                u = e.opposite(v)
                wgt = e.element()
                if d[v] = d[u] + wgt:
                    tree[v] = e
    return tree

