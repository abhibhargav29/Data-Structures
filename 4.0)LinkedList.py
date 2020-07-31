#Making a node class
class Node():
    def __init__(self, val = None):
        self.value= val 
        self.next = None

#Defining class singly linklist
class SinglyLinkedList():
    def __init__(self):
        self.head = None
    
    def array_to_Linklist(self, arr, n):
        self.head = Node(arr[0])
        self.head.next=None
        traverse = self.head
        for i in range(1, n):
            temp = Node(arr[i])
            traverse.next = temp
            traverse=traverse.next
    
    def delete(self,val):
        curr=self.head
        if(curr.value == val):
            self.head = curr.next
            return
        prev = self.head
        curr = curr.next
        while(curr!=None):
            if(curr.value == val):
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next

    def insert(self, val, index=0):
        New = Node(val)
        if(index == 0):
            temp = self.head
            self.head= New
            New.next = temp
            return
        elif(index<0):
            index=-index
            prev = self.head
            while(index>0):
                curr=prev.next
                index-=1
            while(curr!=None):
                prev = curr
                curr = curr.next
            temp = prev.next
            prev.next = New
            New.next = temp
            return
        prev = self.head
        index-=1
        while(index>0):
            prev = prev.next
            index-=1
        temp = prev.next
        prev.next = New
        New.next = temp
        
    def reverse(self):
        prev=self.head
        curr=self.head.next
        prev.next=None
        while(curr!=None):
            next=curr.next
            curr.next= prev
            prev=curr
            curr=next
        self.head = prev

    def display(self):
        traverse = self.head
        while(traverse!=None):
            print(traverse.value, end=" ")
            traverse = traverse.next

#Driver Code checking each function
LL = SinglyLinkedList()
LL.array_to_Linklist([1,2,3,5,7], 5)
print("Array converted to linklist: ",end="")
LL.display()
LL.insert(0,0)
LL.insert(8,-1)
print("After inertions at start and end: ",end="")
LL.display()
LL.delete(7)
print("After deletion of 7: ", end="")
LL.display()
LL.reverse()
print("After reversing: ",end="")
LL.display()
            
