from queue import Queue

class DirectedGraph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(0, self.V)]
        self.indeg = [0 for i in range(0, self.V)]

    def addEdge(self, v1, v2, weight):
        self.graph[v1].append((v2, weight))
        self.indeg[v2]+=1
    
    def removeEdge(self, v1, v2):
        for i in range(len(self.graph[v1])):
            if(self.graph[v1][i][0]==v2):
                del self.graph[v1][i]
                self.indeg[v2]-=1
                break
    
    def printGraph(self): 
        for i in range(self.V):
            if(len(self.graph[i])==0):
                print("vertex",i,"has no out-going edge")
                continue
            print("vertex",i,"has edges to: ",end="")
            for tup in self.graph[i]:
                print(tup[0],"(weight "+str(tup[1])+")",end=" ")
            print()

    def cycleDetectDFS(self):
        visited = [False for i in range(0,self.V)]
        RecStack = [False for i in range(0, self.V)]

        for i in range(self.V):
            if(visited[i]==False and self.DFSUtil(i, visited, RecStack)):
                return True
        return False

    def DFSUtil(self, source, visited, RecStack):
        visited[source] = True
        RecStack[source] = True

        for ele in self.graph[source]:
            if(visited[ele[0]]==False and self.DFSUtil(ele[0], visited, RecStack)):
                return True
            elif(RecStack[ele[0]]==True):
                return True
        RecStack[source] = False
        return False

    def BFSTopologicalSort(self):
        if(self.cycleDetectDFS()==True):
            print("The graph is cyclic, topological sort not possible.")
            return
        
        DegArr = self.indeg 
        q = Queue()
        for i in range(len(DegArr)):
            if(DegArr[i]==0):
                q.put(i)

        while(q.empty()!=True):
            curr = q.get()
            print(curr, end=" ")
            for ele in self.graph[curr]:
                if(DegArr[ele[0]]!=0):
                    DegArr[ele[0]]-=1
                    if(DegArr[ele[0]]==0):
                        q.put(ele[0])
        print()

g = DirectedGraph(5)

g.addEdge(0, 1, 2)
g.addEdge(2, 1, 1)
g.addEdge(2, 3, 3)
g.addEdge(2, 4, 1)
g.addEdge(4, 0, 3)

g.printGraph()
print()

print(g.cycleDetectDFS())
print()

g.BFSTopologicalSort()
print()
