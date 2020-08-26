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

    def insert(self, val):
        self.size+=1
        self.heap.append(val)
        curr = self.size-1
        if(self.parent(curr)==-1):
            return

        while(self.parent(curr)!=-1):
            if(self.heap[curr] < self.heap[self.parent(curr)]):
                self.swap(curr, self.parent(curr))
                curr = self.parent(curr)
            else:
                break

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
    
    def minHeapify(self, pos):
        left = self.left(pos)
        right= self.right(pos)
        smallest = pos

        if(left==-1):
            return
        elif(right==-1):
            if(self.heap[left]<self.heap[pos]):
                self.swap(pos, left)
                return
            else:
                return

        if(self.heap[left] < self.heap[pos] and self.heap[left] < self.heap[right]):
            smallest = left
        elif(self.heap[right] < self.heap[pos] and self.heap[right] < self.heap[left]):
            smallest = right
        
        if(smallest==pos):
            return
        else:
            self.swap(smallest, pos)

    def BuildHeap(self, arr):
        self.heap = arr
        self.size = len(arr)
        for pos in range((self.size-2)//2,-1,-1):
            self.minHeapify(pos)

Heap = minHeap() 

Heap.insert(5) 
Heap.insert(3) 
Heap.insert(17)
Heap.insert(10) 
Heap.insert(84) 
Heap.insert(19) 
Heap.insert(6) 
Heap.insert(22) 
Heap.insert(9)

Heap.printHeap()
print()

arr=[5,3,17,10,84,19,6,22,9]
Heap2 = minHeap()
Heap2.BuildHeap(arr)
Heap2.printHeap()