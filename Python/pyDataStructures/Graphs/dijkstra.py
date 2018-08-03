import heapq
import sys

class Graph:
    
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
    
    def shortest_path(self, start, finish):
        """
        Greedy Technique:
        -Take closest unvisited vertex from start, find distance to all adjacent
        -repeat
        """
        distances = {} # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodesPQ = [] # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodesPQ, [0, vertex])
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodesPQ, [sys.maxsize, vertex])
            previous[vertex] = None
        
        while len(nodesPQ):
            smallest = heapq.heappop(nodesPQ)[1] # Vertex in nodes with smallest distance in distances
            if smallest == finish: # If the closest node is our target we're done so print the path
                path = []
                while previous[smallest]: # Traverse through nodes til we reach the root which is 0
                    path.append(smallest)
                    smallest = previous[smallest]
                path.append(start)
                path.reverse()
                return path
            if distances[smallest] == sys.maxsize: # All remaining vertices are inaccessible from source
                break
            
            for neighbor in self.vertices[smallest]: # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor] # Alternative path distance
                if alt < distances[neighbor]: # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodesPQ:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
            heapq.heapify(nodesPQ)

    def __str__(self):
        return str(self.vertices)

if __name__ == '__main__':
    """
        g = Graph()
        g.add_vertex('A', {'B': 7, 'C': 8})
        g.add_vertex('B', {'A': 7, 'F': 2})
        g.add_vertex('C', {'A': 8, 'F': 6, 'G': 4})
        g.add_vertex('D', {'F': 8})
        g.add_vertex('E', {'H': 1})
        g.add_vertex('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
        g.add_vertex('G', {'C': 4, 'F': 9})
        g.add_vertex('H', {'E': 1, 'F': 3})
        print(g.shortest_path('A', 'H'))
    """
    g = Graph()
    g.add_vertex('A', {'B': 3, 'C': 7, 'D': 8})
    g.add_vertex('B', {'A': 3, 'C': 2, 'E': 5, 'F': 4})
    g.add_vertex('C', {'B': 2, 'G': 1})
    g.add_vertex('D', {'A': 8, 'G': 2})
    g.add_vertex('E', {'H': 6})
    g.add_vertex('F', {'B': 4, 'H': 3})
    g.add_vertex('G', {'C': 1, 'H': 4})
    g.add_vertex('H', {'E': 6, 'F': 3, 'G': 4})
    print(g.shortest_path('A', 'H'))