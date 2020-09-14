from queue import Queue
from ModifiesHeap import minHeap

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
        print(cnt,"component(s) present")


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
        print(cnt,"component(s) present")

    def printGraph(self): 
        for i in range(self.V):
            if(len(self.graph[i])==0):
                print("vertex",i,"has no adjacents")
                continue
            print("vertex",i,"has adjacents: ",end="")
            for tup in self.graph[i]:
                print(tup[0],"(weight "+str(tup[1])+")",end=" ")             
            print()
            
     #Cycle detection in graph, not called in driver code
    def cycleDetect(self):
        visited = [False for i in range(self.V)]
        for i in range(self.V):
            if(visited[i]==False):
                if(self.cycleHelper(i, visited)==True):
                    return True
        return False

    def cycleHelper(self, source, visited, parent=-1):
        visited[source] = True
        for adj in self.graph[source]:
            if(visited[adj[0]]==False):
                if(self.cycleHelper(adj[0], visited, source)):
                    return True
            elif(adj[0]!=parent):
                return True
        return False

    #Shortest path using dijikstra algorihthm, it works for all types of graph except negative weights.
    #It is faster than bellman ford algorithm.
    def Dijikstra(self, source=0):
        distArr = [float('inf') for i in range(self.V)]
        distArr[source] = 0
        Heap = minHeap()
        for i in range(self.V):
            if(i==source):
                Heap.insert(0, i)
            else:
                Heap.insert(2**32, i)
        done=set()
        while(len(done)!=self.V):
            u = Heap.HeapPop()
            if(u[1] in done):
                continue
            done.add(u[1])
            for node in self.graph[u[1]]:
                if(node[0] in done):
                    continue
                dist = node[1]+distArr[u[1]]
                if(dist<distArr[node[0]]):
                    distArr[node[0]]=dist 
                    Heap.decreaseKey(node[0], dist)
        return distArr
    
    #Shortest Path using bellman ford algo, it can work for negative weight edges as well.
    def BellmanFord(self, source):
        distArr = [float('inf') for i in range(self.V)]
        distArr[source] = 0

        for j in range(self.V-1):
            for i in range(self.V):
                for ele in self.graph[i]:
                    if(ele[1]+distArr[i] < distArr[ele[0]]):
                        distArr[ele[0]] = ele[1]+distArr[i]
        
        #This part will detect if their is a negative weight cycle. Negative weight cycle arises when their is a cycle in directed graph
        #such that the traversal over that cycle yeilds negative weight, in such a case shortest path can not be determined.
        for i in range(self.V):
                for ele in self.graph[i]:
                    if(ele[1]+distArr[i] < distArr[ele[0]]):
                        print("Negative weight cycle detected, shortest weight not possible!")
                        return

        return distArr
    
    #Minimum spanning tree using prims algorithm.
    def PrimsMST(self):
        heap = minHeap()
        key = []
        parent = [-1 for i in range(self.V)]
        visited = [False for i in range(self.V)]
        visited[0] = True

        for i in range(self.V):
            if(i==0):
                key.append(0)
                heap.insert(0, 0)
                continue
            key.append(float('inf'))
            heap.insert(key[i], i)
        
        while(heap.size>0):
            v = heap.HeapPop()
            visited[v[1]] = True
            for ele in self.graph[v[1]]:
                if(visited[ele[0]]==False and ele[1]<key[ele[0]]):
                    key[ele[0]] = ele[1]
                    parent[ele[0]] = v[1]
                    heap.decreaseKey(ele[0],ele[1])
        
        for i in range(self.V):
            if(parent[i]==-1):
                continue
            #Each edge
            print(parent[i], "-", i)
        print("MST WEIGHT: ", sum(key))

#Driver code
V = 5
graph = Graph(V)


#Insertions
graph.addEdge(0, 1, 1) 
graph.addEdge(0, 4, 2)
graph.addEdge(1, 2, 3) 
graph.addEdge(1, 3, 1) 
graph.addEdge(1, 4, 2)  
graph.addEdge(2, 3, 1)
graph.addEdge(3, 4, 3)  


#Graph
print("Graph: ")
graph.printGraph() 
print()


#Traversals
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


#Shortest Path
print("Shortest paths from 0:", end=" ")
print(graph.Dijikstra(0))
print()

print("Shortest paths from 0:", end=" ")
print(graph.BellmanFord(0))
print()

#MST
print("MST Edges:")
graph.PrimsMST()
print()
