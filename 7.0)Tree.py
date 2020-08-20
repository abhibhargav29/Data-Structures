#Tree Class
class Tree():
    #Class variable so that its available to all recursive calls in height method.
    Diameter=0
    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right= None
    
    #The Three DFS traversals.
    def Inorder(self):
        if(self.left!=None):
            self.left.Inorder()
        print(self.val, end=" ")
        if(self.right!=None):
            self.right.Inorder()
    def Preorder(self):
        print(self.val, end=" ")
        if(self.left!=None):
            self.left.Preorder()
        if(self.right!=None):
            self.right.Preorder()
    def Postorder(self):
        if(self.left!=None):
            self.left.Postorder()
        if(self.right!=None):
            self.right.Postorder()
        print(self.val, end=" ")
        
    #BFS(each level printed seperately)
    def Levelorder(self):
        q=[]
        if(self.val==None):
            return
        q.append(self)
        #This none helps to seperate each level
        q.append(None)
        while(len(q)>1):
            curr = q[0]
            del q[0]
            #If curr=none, we have traversed one level
            if(curr==None):   
                print("|",end=" ")
                q.append(None)
                continue
            print(curr.val, end=" ")
            if(curr.left!=None):
                q.append(curr.left)
            if(curr.right!=None):
                q.append(curr.right)
    
    #Spiral Traversal using 2 stacks.
    def Spiral(self):
        stk1=[]
        stk2=[]
        if(self.val==None):
            return 
        stk1.append(self)
        while(stk1 or stk2):
            while(stk1):
                curr=stk1.pop()
                if(curr.left!=None):
                    stk2.append(curr.left)
                if(curr.right!=None):
                    stk2.append(curr.right)
                print(curr.val, end=" ")
            print("|", end=" ")
            while(stk2):
                curr=stk2.pop()
                #Append in reverse manner in this stack.
                if(curr.right!=None):
                    stk1.append(curr.right)
                if(curr.left!=None):
                    stk1.append(curr.left)
                print(curr.val, end=" ")
            print("|", end=" ")
    
    #Number of nodes
    def size(self):
        if(self.val==None):
            return 0
        if(self.left!=None and self.right!=None):
            return 1+self.left.size()+self.right.size()
        elif(self.left!=None and self.right==None):
            return 1+self.left.size()
        elif(self.left==None and self.right!=None):
            return 1+self.right.size()
        else:
            return 1

    #Kth level nodes
    def k_Level(self, k):
        if(self.val==None):
            return
        if(k==0):
            print(self.val, end=" ")
        elif(k<0):
            return
        else:
            if(self.left!=None):
                self.left.k_Level(k-1)
            if(self.right!=None):
                self.right.k_Level(k-1)
    
    #Not Called in driver code
    def CompleteTreeSize(self):
        if(self.val==None):
            return 0
        leftTraverse=self.left
        leftH=0
        while(leftTraverse!=None):
            leftTraverse=leftTraverse.left
            leftH+=1
        rightTraverse=self.right
        rightH=0
        while(rightTraverse!=None):
            rightTraverse=rightTraverse.left
            rightH+=1
        if(leftH==rightH):
            return 2**leftH-1
        else:
            return 1 + self.left.CompleteTreeSize() + self.right.CompleteTreeSize()
    
    #Height method returns height and if True parameter passed, diameter as well.
    def height(self, diameter=False):
        if(self.val==None):
            return 0
        if(self.left!=None):
            lefth = self.left.height()
        else:
            lefth=0
        if(self.right!=None):
            righth= self.right.height()
        else:
            righth=0
        Diameter = max(diameter, lefth+righth+1)
        if(diameter):
            return max(lefth,righth)+1, Diameter
        return max(lefth,righth)+1
    
    #To get a hash map with only top nodes as values and key as their horizontal distance from root.
    def getVerticalMap(root, m, level=0, priority=0):
    if(root==None):
        return
    if(level not in m):
        m[level]=[root.info, priority]
    elif(m[level][1]>priority):
        m[level]=[root.info, priority]

    getVerticalMap(root.left, m, level-1, priority+1)
    getVerticalMap(root.right,m, level+1, priority+1)

    #Print top view using hash map.
    def topView(root):
        Map={}
        getVerticalMap(root, Map)
        for i in sorted(Map.keys()):
            print(Map[i][0], end=" ")
    
    
#Function to contruct tree from preorder and inorder.
#Not called in driver code.
def ConstructTree(InOrd, PreOrd, InStart, InEnd):
    if(InStart>InEnd):
        return None
    #Give PreIndex as static variable at time of calling function like this:
    #ConstructTree.PreIndex = 0
    Node = Tree(PreOrd[ConstructTree.PreIndex])
    ConstructTree.PreIndex+=1
    #Search for given data in only the start and end window of array.
    #This search fails if there is duplication of values in numbers, so one can use alphabets.
    InIndex=0
    for i in range(InStart,InEnd+1):
        if(InOrd[i]==Node.val):
            InIndex=i
            break
    Node.left = ConstructTree(InOrd, PreOrd, InStart, InIndex-1)
    Node.right= ConstructTree(InOrd, PreOrd, InIndex+1, InEnd)
    return Node  

#Driver Code
#Tree Making
T = Tree()
T.val = 1
T.left = Tree(2)
T.right= Tree(3)
T.left.left = Tree(4)
T.left.right= Tree(5)
T.right.left = Tree(6)
T.right.right= Tree(7)

#Tree size
print("Tree size: ",T.size())

#Tree Height and Diameter
h,d = T.height(True)
print("Height:",h,"Diameter:",d)

#Nodes at kth level
print("Nodes at 2nd Level: ",end="")
T.k_Level(2)
print()

#DFS Traversals
print("PreOrder Traversal: ", end="")
T.Preorder()
print()
print("InOrder Traversal: ", end="")
T.Inorder()
print()
print("PostOrder Traversal: ", end="")
T.Postorder()
print()

#BFS Traversal with each level seperated by "|"
print("LevelOrder Traversal: ", end="")
T.Levelorder()

#Spiral Trvaersal
print("Spiral Traversal: ",end="")
T.Spiral()
