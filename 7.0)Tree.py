#Tree Class
class Tree():
    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right= None

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
