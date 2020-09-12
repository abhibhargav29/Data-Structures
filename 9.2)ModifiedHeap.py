class minHeap():
    def __init__(self):
        self.size = 0 
        self.heap = []
        self.pos = dict()
    
    def parent(self, pos):
        if(pos==0):
            return -1
        return (pos-1)//2

    def left(self, pos):
        ans = 2*pos+1
        if(ans>=self.size):
            return -1
        return ans

    def right(self, pos):
        ans = 2*pos+2
        if(ans>=self.size):
            return -1
        return ans

    def swap(self, i, j):
        self.pos[self.heap[i][1]] = j
        self.pos[self.heap[j][1]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    #Insert while maintaining heap property.
    def insert(self, val, vertex):
        self.size+=1
        #Add the value at end of the array
        self.heap.append([val, vertex])
        curr = self.size-1
        self.pos[vertex] = curr
        
        #The case if its the first element that we inserted
        if(self.parent(curr)==-1):
            return

        while(self.parent(curr)!=-1):
            if(self.heap[curr][0] < self.heap[self.parent(curr)][0]):
                self.swap(curr, self.parent(curr))
                curr = self.parent(curr)
            else:
                break
    
    #It takes in a position in array and fixes the heap formed from this node as root assuming all below are in order.
    def minHeapify(self, pos):
        left = self.left(pos)
        right= self.right(pos)

        #No child
        if(left==-1):
            return
        #No right child
        elif(right==-1):
            if(self.heap[left][0]<self.heap[pos][0]):
                self.swap(pos, left)
                return
            else:
                return

        if(self.heap[left][0] < self.heap[pos][0] and self.heap[left][0] < self.heap[right][0]):
            self.swap(pos, left)
            #Fix the nodes in left part now.
            self.minHeapify(left)
        elif(self.heap[right][0] < self.heap[pos][0] and self.heap[right][0] < self.heap[left][0]):
            self.swap(pos, right)
            #Fix the nodes in right part now.
            self.minHeapify(right)
        else:
            return
    
    #Method not called in driver code. 
    #It pops the topmost node or the min element.
    def HeapPop(self):
        item = self.heap[0]
        self.swap(0,self.size-1)
        del self.heap[self.size-1]
        self.size-=1
        self.minHeapify(0)
        return item

    def decreaseKey(self, vertex, val):
        pos = self.pos[vertex]
        self.heap[pos][0] = val
        if(self.parent(pos)==-1):
            return
        while(self.parent(pos)!=-1):
            if(self.heap[self.parent(pos)][0]>self.heap[pos][0]):
                self.swap(self.parent(pos), pos)
                pos=self.parent(pos)
            else:
                break
