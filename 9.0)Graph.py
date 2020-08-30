class AdjNode():
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None]*vertices

    def addEdge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 
