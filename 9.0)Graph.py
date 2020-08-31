class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for j in range(vertices)]

    def addEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
  
    def printGraph(self): 
        for i in range(self.V):
            if(len(self.graph[i])==0):
                continue
            print("vertex",i,"has adjacents: ",end="")
            print(" ".join(map(str, self.graph[i])))

V = 5
graph = Graph(V)
graph.addEdge(0, 1) 
graph.addEdge(0, 4) 
graph.addEdge(1, 2) 
graph.addEdge(1, 3) 
graph.addEdge(1, 4) 
graph.addEdge(2, 3) 
graph.addEdge(3, 4) 
   
graph.printGraph() 
