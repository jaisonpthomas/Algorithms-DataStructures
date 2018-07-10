from graph import *

#Vertex Creation
g = Graph(directed = True)
C0 = g.insertVertex("C0")
C1 = g.insertVertex("C1")
C2 = g.insertVertex("C2")
C3 = g.insertVertex("C3")
C4 = g.insertVertex("C4")
C5 = g.insertVertex("C5")
C6 = g.insertVertex("C6")

#Edge Creation
g.insertEdge(C0,C1)
g.insertEdge(C0,C2)
g.insertEdge(C0,C5)
g.insertEdge(C1,C4)
g.insertEdge(C3,C2)
g.insertEdge(C3,C4)
g.insertEdge(C3,C5)
g.insertEdge(C3,C6)
g.insertEdge(C5,C2)
g.insertEdge(C6,C0)
g.insertEdge(C6,C4)


print(g)

def topologicalSort(g):
    topo = []
    ready = []
    inCount = {}

    for u in g.vertices():
        inCount[u] = g.degree(u, False)
        if inCount[u] == 0:
            ready.append(u)
    while len(ready):
        u = ready.pop()
        topo.append(u)
        for e in g.incidentEdges(u):
            v = e.opposite(u)
            inCount[v] -= 1
            if inCount[v] == 0:
                ready.append(v)
            
    return topo

print("---Topological Sort---")
topoList = topologicalSort(g)
for vertex in topoList:
    print(vertex, end = " -> ") 
