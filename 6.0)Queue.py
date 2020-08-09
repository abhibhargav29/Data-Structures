#Queue Class
class Queue():
    #Size holds number of elements and capacity has the actual capacity
    def __init__(self, capacity=10):
        self.arr=[0]*capacity
        self.cap=capacity
        self.front=None
        self.rear=None
        self.size=0
    
    def addElement(self, x):
        if(self.size==self.cap):
            print("Queue Full")
            return
        elif(self.size==0):
            self.front=self.rear=0
            self.arr[self.rear]=x
            self.size+=1
            return
        self.rear = (self.rear+1)%self.cap
        self.arr[self.rear] = x
        self.size+=1

    def delElement(self):
        if(self.size==0):
            print("Queue Empty")
            return
        elif(self.size==1):
            x = self.arr[self.front]
            self.front=self.rear=None
            print(x,"Deleted")
            self.size-=1
            return
        x = self.arr[self.front]
        self.front=(self.front+1)%self.cap
        self.size-=1
        print(x,"Deleted")
        
    def show(self):
        if(self.size==0):
            print("Empty")
            return
        traverse=self.front
        while(traverse!=self.rear):
            print(self.arr[traverse], end=" ")
            traverse=(traverse+1)%self.cap
        print(self.arr[traverse])

#Driver code
Q = Queue(7)
Q.addElement(1)
Q.addElement(2)
Q.addElement(3)
Q.addElement(4)
Q.addElement(5)
Q.addElement(6)
Q.addElement(7)
Q.show()

#Trying to add after full
Q.addElement(8)

#Deletion
Q.delElement()
Q.show()

#Adding after rear reaches end but array has space still
Q.addElement(8)
Q.show()
