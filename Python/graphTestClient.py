from graph import *

#Vertex Creation
g = Graph(directed = True)
BOS = g.insertVertex("BOS")
JFK = g.insertVertex("JFK")
DFW = g.insertVertex("DFW")
LAX = g.insertVertex("LAX")
ORD = g.insertVertex("ORD")
MIA = g.insertVertex("MIA")
SFO = g.insertVertex("SFO")

#Edge Creation
g.insertEdge(BOS, JFK)
g.insertEdge(BOS, MIA)
g.insertEdge(BOS, SFO)

g.insertEdge(JFK, BOS)
g.insertEdge(JFK, DFW)
g.insertEdge(JFK, MIA)
g.insertEdge(JFK, SFO)

g.insertEdge(DFW, LAX)
g.insertEdge(DFW, ORD)
g.insertEdge(DFW, SFO)

g.insertEdge(LAX, ORD)

g.insertEdge(ORD, DFW)
g.insertEdge(ORD, MIA)

g.insertEdge(MIA, DFW)
g.insertEdge(MIA, LAX)

g.insertEdge(SFO, LAX)


##Test Code
result = {BOS: None}
DFS(g, BOS, result)

print("-POINT-", "-ROUTE-", sep = "   ")
print()
for key in result:
    print(key, ":     ", result[key])
##