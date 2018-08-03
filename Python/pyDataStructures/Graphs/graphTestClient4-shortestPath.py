
g = Graph(directed = True)

A = g.insertVertex("A")
B = g.insertVertex("B")
C = g.insertVertex("C")
D = g.insertVertex("D")
E = g.insertVertex("E")
F = g.insertVertex("F")
G = g.insertVertex("G")
H = g.insertVertex("H")

g.insertEdge(A,B,3)
g.insertEdge(A,C,7)
g.insertEdge(A,D,8)

g.insertEdge(B,A,3)
g.insertEdge(B,C,2)
g.insertEdge(B,E,5)
g.insertEdge(B,F,4)

g.insertEdge(C,B,2)
g.insertEdge(C,G,1)

g.insertEdge(D,A,8)
g.insertEdge(D,G,2)

g.insertEdge(E,H,6)

g.insertEdge(F,B,4)
g.insertEdge(F,H,3)

g.insertEdge(G,C,1)
g.insertEdge(G,H,4)

g.insertEdge(H,E,6)
g.insertEdge(H,F,3)
g.insertEdge(H,G,4)

shortPath = shortestPath(g, A, H, True)

#['A', 'B', 'C', 'G', 'H']