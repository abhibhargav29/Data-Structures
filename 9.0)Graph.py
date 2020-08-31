from queue import Queue

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for j in range(vertices)]

    def addEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    
    def removeEdge(self, v1, v2):
        for i in range(len(self.graph[v1])):
            if(self.graph[v1][i]==v2):
                del self.graph[v1][i]
                break
        for j in range(len(self.graph[v2])):
            if(self.graph[v2][j]==v1):
                del self.graph[v2][j]
                break

    def BFS(self, source=0):
        Q = Queue()
        Q.put(source)
        visited=[False for i in range(self.V)]
        visited[source]=True
        while(Q.empty()!=True):
            curr = Q.get()
            print(curr, end=" ")
            for ele in self.graph[curr]:
                if(visited[ele]==False):
                    Q.put(ele)
                    visited[ele]=True
        print()

    def DFS(self, source=0):
        visited = [False for i in range(self.V)]
        self.DFSHelper(source, visited)
        print()

    def DFSHelper(self, source, visited):
        visited[source] = True
        print(source, end=" ")

        for ele in self.graph[source]:
            if(visited[ele]==False):
                self.DFSHelper(ele, visited)

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
   
print("Graph: ")
graph.printGraph() 
print()

print("BFS Traversal from 0: ")
graph.BFS(0)

print("DFS Traversal from 0: ")
graph.DFS(0)
