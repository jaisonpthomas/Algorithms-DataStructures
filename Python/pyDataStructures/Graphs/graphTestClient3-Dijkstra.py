from graph import *

def shortestPathLengths(g, src):
    d = {}
    cloud = {}
    pq = AdaptableHeapPriorityQueue()
    pqlocator = {}

    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')
        pqlocator[v] = pq.add(d[v], v)

    while not pq.isEmpty():
        key, u = pq.removeMin()
        cloud[u] = key
        del pqlocator[u]
        for e in g.incidentEdges(u):
            v = e.opposite(u)
            if v not in cloud:
                wgt = e.element()
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt
                    pq.update(pqlocator[v], d[v], v)

    return cloud

#Vertex Creation
g = Graph(directed = False)
BOS = g.insertVertex("BOS")
BWI = g.insertVertex("BWI")
DFW = g.insertVertex("DFW")
JFK = g.insertVertex("JFK")
LAX = g.insertVertex("LAX")
MIA = g.insertVertex("MIA")
ORD = g.insertVertex("ORD")
PVD = g.insertVertex("PVD")
SFO = g.insertVertex("SFO")

#Edge Creation
g.insertEdge(BOS, JFK, 187)
g.insertEdge(BOS, MIA, 1258)
g.insertEdge(BOS, ORD, 867)
g.insertEdge(BOS, SFO, 2704)

g.insertEdge(BWI, JFK, 184)
g.insertEdge(BWI, MIA, 946)
g.insertEdge(BWI, ORD, 621)

g.insertEdge(DFW, JFK, 1391)
g.insertEdge(DFW, LAX, 1235)
g.insertEdge(DFW, MIA, 1121)
g.insertEdge(DFW, ORD, 802)
g.insertEdge(DFW, SFO, 1464)

g.insertEdge(JFK, MIA, 1090)
g.insertEdge(JFK, ORD, 740)
g.insertEdge(JFK, PVD, 144)

g.insertEdge(LAX, MIA, 2342)
g.insertEdge(LAX, SFO, 337)

g.insertEdge(ORD, PVD, 849)
g.insertEdge(ORD, SFO, 1846)

print(g)