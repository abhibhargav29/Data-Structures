class minHeap():
    def __init__(self):
        self.size = 0 
        self.heap = []
    
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
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    #Insert while maintaining heap property.
    def insert(self, val):
        self.size+=1
        #Add the value at end of the array
        self.heap.append(val)
        curr = self.size-1
        
        #The case if its the first element that we inserted
        if(self.parent(curr)==-1):
            return

        while(self.parent(curr)!=-1):
            if(self.heap[curr] < self.heap[self.parent(curr)]):
                self.swap(curr, self.parent(curr))
                curr = self.parent(curr)
            else:
                break

    #Display heap as parent and child
    def printHeap(self):
        if(self.size==0):
            print("Empty Heap")
            return
        for i in range(self.size//2):
            print("Parent: ", self.heap[i], end=" ")
            if(self.left(i)!=-1):
                print("Left child: ", self.heap[self.left(i)], end=" ")
            else:
                break
            if(self.right(i)!=-1):
                print("Right child: ", self.heap[self.right(i)], end=" ")
            else:
                break
            print()
    
    #Helper for build heap
    #It takes in a position in array and fixes the heap formed from this node as root.
    def minHeapify(self, pos):
        left = self.left(pos)
        right= self.right(pos)

        #No child
        if(left==-1):
            return
        #No right child
        elif(right==-1):
            if(self.heap[left]<self.heap[pos]):
                self.swap(pos, left)
                return
            else:
                return

        if(self.heap[left] < self.heap[pos] and self.heap[left] < self.heap[right]):
            self.swap(pos, left)
            #Fix the nodes in left part now.
            self.minHeapify(left)
        elif(self.heap[right] < self.heap[pos] and self.heap[right] < self.heap[left]):
            self.swap(pos, right)
            #Fix the nodes in right part now.
            self.minHeapify(right)
        else:
            return

    #Makes heap from array
    def BuildHeap(self, arr):
        self.heap = arr
        self.size = len(arr)
        #Call heapify starting from the bottom most non leaf node.
        #This node is the parent of last node, so it will be at (size-2)//2 position
        for pos in range((self.size-2)//2,-1,-1):
            self.minHeapify(pos)
    
    #Method not called in driver code. 
    #It pops the topmost node or the min element.
    def HeapPop(self):
        if(heap.size==0):
            print("Empty heap")
            return None
        item = self.heap[0]
        self.swap(0,self.size-1)
        del self.heap[self.size-1]
        self.size-=1
        self.minHeapify(0)
        return item
    
    def DecreaseKey(self, pos, val):
        self.heap[pos] = val
        if(self.parent(pos)==-1):
            return
        while(self.parent(pos)!=None):
            if(self.heap[self.parent(pos)]>self.heap[pos]):
                self.swap(self.parent(pos), pos)
                pos=self.parent(pos)
            else:
                break

#Driver Code
Heap1 = minHeap() 

#Insertions
Heap1.insert(5) 
Heap1.insert(3) 
Heap1.insert(17)
Heap1.insert(10) 
Heap1.insert(84) 
Heap1.insert(19) 
Heap1.insert(6) 
Heap1.insert(22) 
Heap1.insert(9)

#Display Heap
print("Heap Made After Insertions: ")
Heap1.printHeap()
print()

#Build heap from array
arr=[5,3,17,10,84,19,6,22,9]
Heap2 = minHeap()
Heap2.BuildHeap(arr)

#Display this Heap
print("Heap Made From Array: ")
Heap2.printHeap()
