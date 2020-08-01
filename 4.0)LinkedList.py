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
                #If we want to delete each and every occurence we will remove this break statement.
                break
            prev = curr
            curr = curr.next

    def insert(self, val, index=0):
        New = Node(val)
        #Insert at beginning
        if(index == 0):
            temp = self.head
            self.head= New
            New.next = temp
            return
        #Negative index means insert at this index counting from last, so we use two ptr approach.
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
        #The positive index case
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
            
    #Method to reverse given list  
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
    
    #Method that places even elements at front and odd at back
    #It maintains order between two even or odd elements
    def segregate(self):
        evenH=None
        oddH=None
        evenT=None
        oddT=None
        traverse=self.head
        while(traverse!=None):
            if(traverse.value%2==0):
                if(evenH==None):
                    evenH=traverse
                    evenT=traverse
                else:
                    evenT.next=traverse
                    evenT=traverse
            else:
                if(oddH==None):
                    oddH=traverse
                    oddT=traverse
                else:
                    oddT.next=traverse
                    oddT=traverse
            traverse=traverse.next

        if(oddH==None or evenH==None):
            return
        evenT.next=oddH
        oddT.next=None
        self.head=evenH

    #This method makes a link from end to the element with given index n
    def make_loop(self, n):
        traverse=self.head
        end=self.head
        cnt=0
        while(traverse!=None and cnt<n):
            traverse=traverse.next
            end=end.next
            cnt+=1
        while(end.next!=None):
            end=end.next
        end.next=traverse
        print("Loop made by linking",end.value,"to",traverse.value)
        
    #This method removes any link if present
    def remove_loop(self):
        slow=self.head
        fast=self.head
        flag=0
        while(fast!=None or fast.next!=None):
            slow=slow.next
            fast=(fast.next).next
            if(slow==fast):
                flag=1
                break
        if(flag==0):
            print("No loop present")
            return
        slow=self.head
        while(slow.next!=fast.next):
            slow=slow.next
            fast=fast.next
        fast.next=None

#Driver Code checking each function
LL = SinglyLinkedList()

#Storing in LL
LL.array_to_Linklist([1,2,3,5,7], 5)
print("Array converted to linklist: ",end="")
LL.display()

#Insertion
LL.insert(0,0)
LL.insert(8,-1)
print("After inertions at start and end: ",end="")
LL.display()

#Deletion
LL.delete(7)
print("After deletion of 7: ", end="")
LL.display()

#Reversing
LL.reverse()
print("After reversing: ",end="")
LL.display()

#Segregation
LL.segregate()
print("After seperating: ",end="")
LL.display()

#We introduce a loop and then remove it, note that if you call display method after making loop, the you will
#be stuck in an infinte loop while printing.
LL.make_loop(2)
LL.remove_loop()
print("Loop removed: ",end="")
LL.display()
            
