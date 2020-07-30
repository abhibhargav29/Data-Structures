class Node():
    def __init__(self, val = None):
        self.value= val 
        self.next = None

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
        prev = self.head
        index-=1
        while(index>0):
            prev = prev.next
            index-=1
        temp = prev.next
        prev.next = New
        New.next = temp

    def display(self):
        traverse = self.head
        while(traverse!=None):
            print(traverse.value, end=" ")
            traverse = traverse.next

LL = SinglyLinkedList()
LL.array_to_Linklist([1,2,3,5,7], 5)
LL.insert(0,0)
LL.delete(7)
LL.display()
            