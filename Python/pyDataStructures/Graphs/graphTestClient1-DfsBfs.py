from graph import *

def DFS(g, s):
    discovered = {s:None}
    stack = [s]
    while len(stack):
        u = stack.pop()
        for e in g.incidentEdges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                stack.append(v)
    return discovered

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

#print("--- GRAPH G (Airport Routes) ---")
#print(g)
#print()


##Test Code

#print(g.edgeCount())

##DFS Tests
resultDFS = DFS(g, BOS)

print("-POINT-", "-ROUTE-", sep = "   ")
print()
for key in resultDFS:
    print(key, ":     ", resultDFS[key])

print()
    
alpha = constructPath(BOS, MIA, resultDFS)
for vertex in alpha:
    print(vertex, end = " -> ")
print()
print()

        
def BFS(g, s, discovered):
    level = [s]
    while len(level):
        nextLevel = []
        for u in level:
            for e in g.incidentEdges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    nextLevel.append(v)
        level = nextLevel




resultBFS = BFS(g, BOS)
print("*********BFS**********")
print()

print("-POINT-", "-ROUTE-", sep = "   ")
print()
for key in resultBFS:
    print(key, ":     ", resultBFS[key])
