class BST():
    def __init__(self, data=None):
        self.val = data
        self.left= None
        self.right=None

    def insert(self, value):
        if(self.val == None):
            self.val = value
            return
        curr=self
        parent=None
        while(curr!=None):
            parent=curr
            if(curr.val<value):
                curr=curr.right
            elif(curr.val>value):
                curr=curr.left
            else:
                return
        if(parent.val>value):
            parent.left = BST(value)
        else:
            parent.right= BST(value)
    
    def search(self, value):
        if(self.val == None):
            print(value,"Not Found")
            return
        curr=self
        while(curr!=None):
            if(curr.val == value):
                print(value,"Found")
                return
            elif(curr.val > value):
                curr=curr.left
            else:
                curr=curr.right
        print(value,"Not Found")

    def minValueNode(self):
        curr=self
        while(curr.left!=None):
            curr=curr.left
        return curr

    def delete(self, value):
        if(self==None):
            return self

        if(value<self.val):
            self.left = self.left.delete(value)
        elif(value>self.val):
            self.right = self.right.delete(value)
        else:
            if(self.left==None):
                temp=self.right
                self=None
                return temp
            elif(self.right==None):
                temp=self.left
                self=None
                return temp
            temp = self.right.minValueNode()  
            self.val = temp.val  
            self.right = self.right.delete(temp.val)
        return self

    def ceil(self, value):
        if(self.val==None):
            return None
        ans=float('inf')
        curr=self
        while(curr!=None):
            if(curr.val>value):
                ans = min(curr.val, ans)
                curr=curr.left
            elif(curr.val<value):
                curr=curr.right
            else:
                return -1
        if(ans==float('inf')):
            return -1
        return ans    

    def floor(self, value):
        if(self.val==None):
            return None
        ans=-1
        curr=self
        while(curr!=None):
            if(curr.val<value):
                ans = max(curr.val, ans)
                curr=curr.right
            elif(curr.val>value):
                curr=curr.left
            else:
                return -1
        return ans

    def Levelorder(self):
        q=[]
        if(self.val==None):
            return
        q.append(self)
        q.append(None)
        while(len(q)>1):
            curr = q[0]
            del q[0]
            if(curr==None):   
                print("|",end=" ")
                q.append(None)
                continue
            print(curr.val, end=" ")
            if(curr.left!=None):
                q.append(curr.left)
            if(curr.right!=None):
                q.append(curr.right)

Tree = BST()
Tree.insert(30)
Tree.insert(20)
Tree.insert(40)
Tree.insert(20)
Tree.insert(10)
Tree.insert(25)
Tree.insert(35)
Tree.insert(50)

Tree.search(20)
Tree.search(15)

Tree.Levelorder()
print()

Tree.delete(20)

Tree.Levelorder()
print()