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
    

T = Tree()
T.val = 1
T.left = Tree(2)
T.right= Tree(3)

T.left.left = Tree(4)
T.left.right= Tree(5)

T.right.left = Tree(6)
T.right.right= Tree(7)

print("PreOrder Traversal: ", end="")
T.Preorder()
print()
print("InOrder Traversal: ", end="")
T.Inorder()
print()
print("PostOrder Traversal: ", end="")
T.Postorder()
