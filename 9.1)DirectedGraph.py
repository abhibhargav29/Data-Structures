from queue import Queue

class DirectedGraph():
    #indegree array is there to use for Kahns algorithm
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

    #BFS Cycle detection using indegree array.
    def cycleDetectBFS(self):
        DegArr = self.indeg 
        q = Queue()
        for i in range(len(DegArr)):
            if(DegArr[i]==0):
                q.put(i)

        while(q.empty()!=True):
            curr = q.get()
            for ele in self.graph[curr]:
                if(DegArr[ele[0]]!=0):
                    DegArr[ele[0]]-=1
                    if(DegArr[ele[0]]==0):
                        q.put(ele[0])
        if(all(DegArr)):
            return True
        else:
            return False

    #DFS cycle detection by using recusrion stack for ancestors.
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

    #Topological sorting using Kahn's BFS based algorithm.
    def BFSTopologicalSort(self):
        if(self.cycleDetectDFS()==True):
            print("The graph is cyclic, topological sort not possible.")
            return
        
        DegArr = self.indeg     #To not change the indegree array
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

    #Topological Sorting using DFS based approach.
    def DFSTopologicalSort(self):
        visited = [False for i in range(self.V)]
        stack = []

        for i in range(self.V):
            if(visited[i]==False):
                self.DFSTopologicalSortUtil(i, visited, stack)

        return stack

    def DFSTopologicalSortUtil(self, source, visited, stack):
        visited[source] = True

        for ele in self.graph[source]:
            if(visited[ele[0]]==False):
                self.DFSTopologicalSortUtil(ele[0], visited, stack)

        stack.insert(0,source)

    #Special shortest path algorithm for Directed Acyclic graph.
    def ShortestDistance(self, source):
        if(self.cycleDetectBFS()):
            return

        Arr = self.DFSTopologicalSort()
        distArr = [float('inf') for i in range(self.V)]
        distArr[source] = 0

        for i in Arr:
            for ele in self.graph[i]:
                if(distArr[ele[0]]>distArr[i]+ele[1]):
                    distArr[ele[0]] = distArr[i]+ele[1]
        return distArr

    #Reverse all edges of a graph and store it to a new graph
    #Used in kosaraju algo and not called in code
    def reverseGraph(self):
        new = DirectedGraph(self.V)

        for vertex in range(self.V):
            for adj in self.graph[vertex]:
                new.addEdge(adj[0], vertex, adj[1])

        return new

    #DFS search from a source used in kosaraju's algorithm
    def DFS(self, source, visited):
        visited[source] = True
        print(source, end=" ")

        for adj in self.graph[source]:
            if(visited[adj[0]]==False):
                self.DFS(adj[0], visited)

    #Kosaraju algorithm for strongly connected components
    def StronglyConnected(self):
        arr = self.DFSTopologicalSort()
        reverse = self.reverseGraph()
        visited = [False for i in range(self.V)]
        for ele in arr:
            if(visited[ele]==False):
                reverse.DFS(ele, visited)
                print()

#Driver Code
g = DirectedGraph(5)

#Insert edges
g.addEdge(0, 1, 2)
g.addEdge(2, 1, 1)
g.addEdge(2, 3, 3)
g.addEdge(2, 4, 1)
g.addEdge(4, 0, 3)

#Graph
print("Graph: ")
g.printGraph()
print()

#Topologicla sort, only come for not cyclic graph
print("Topological Sort: ", end="")
g.BFSTopologicalSort()
print()

#Shortest distance
print("Distance from 2: ", end="")
print(g.ShortestDistance(2))

#Strongly connected components
print("Strong components: ")
g.StronglyConnected()
