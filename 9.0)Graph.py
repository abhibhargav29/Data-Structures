from queue import Queue

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for j in range(vertices)]

    def addEdge(self, v1, v2, weight):
        self.graph[v1].append((v2, weight))
        self.graph[v2].append((v1, weight))
    
    def removeEdge(self, v1, v2):
        for i in range(len(self.graph[v1])):
            if(self.graph[v1][i][0]==v2):
                del self.graph[v1][i]
                break
        for j in range(len(self.graph[v2])):
            if(self.graph[v2][j][0]==v1):
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
                if(visited[ele[0]]==False):
                    Q.put(ele[0])
                    visited[ele[0]]=True
        print()

    def DisconectedBFS(self):
        visited=[False for i in range(self.V)]
        cnt=0
        for i in range(self.V):
            if(visited[i]==False):
                print("||", end=" ")
                Q = Queue()
                source = i
                Q.put(source)
                visited[source]=True
                while(Q.empty()!=True):
                    curr = Q.get()
                    print(curr, end=" ")
                    for ele in self.graph[curr]:
                        if(visited[ele[0]]==False):
                            Q.put(ele[0])
                            visited[ele[0]]=True
                cnt+=1
        print()
        print(cnt,"components present")


    def DFS(self, source=0):
        visited = [False for i in range(self.V)]
        self.DFSHelper(source, visited)
        print()

    def DFSHelper(self, source, visited):
        visited[source] = True
        print(source, end=" ")

        for ele in self.graph[source]:
            if(visited[ele[0]]==False):
                self.DFSHelper(ele[0], visited)

    def DisconnectedDFS(self):
        visited = [False for i in range(self.V)]
        cnt=0
        for i in range(self.V):
            if(visited[i]==False):
                print("||", end=" ")
                self.DFSHelper(i, visited)
                cnt+=1
        print()
        print(cnt,"components present")

    def printGraph(self): 
        for i in range(self.V):
            if(len(self.graph[i])==0):
                print("vertex",i,"has no adjacents",end="")
                continue
            print("vertex",i,"has adjacents: ",end="")
            for tup in self.graph[i]:
                print(tup[0],"(weight "+str(tup[1])+")",end=" ")
            print()
            

V = 9
graph = Graph(V)
graph.addEdge(0, 1, 1) 
graph.addEdge(0, 4, 2)
graph.addEdge(1, 2, 3) 
graph.addEdge(1, 3, 1) 
graph.addEdge(1, 4, 2)  
graph.addEdge(2, 3, 1)
graph.addEdge(3, 4, 3)  

graph.addEdge(5, 6, 1)
graph.addEdge(5, 8, 1)
graph.addEdge(6, 7, 1) 
   
print("Graph: ")
graph.printGraph() 
print()

print("BFS Traversal from 0: ")
graph.BFS(0)
print()

print("DFS Traversal from 0: ")
graph.DFS(0)
print()

print("BFS Traversal for disconnected: ")
graph.DisconectedBFS()
print()

print("DFS Traversal for disconnected: ")
graph.DisconnectedDFS()
print()
