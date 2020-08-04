class Stack():
    def __init__(self, arr=[]):
        self.mainArr= arr
        self.size = len(arr)

    def push(self, element):
        self.mainArr.append(element)
        self.size +=1

    def pop(self, ret=False):
        if(self.size==0):
            print("Underflow")
            return False
        element=self.mainArr[-1]
        del self.mainArr[-1]
        self.size-=1
        if(ret==True):
            return element

    def topElement(self):
        if(self.size==0):
            return False
        return self.mainArr[-1]

def isBalParenthesis(string):
    s = Stack()
    opening = ["(","{","["]
    closing = [")","}","]"]
    for i in range(len(string)):
        if(string[i] in opening):
            s.push(string[i])
        else:
            if(s.topElement()==False):
                return False
            index1 = opening.index(s.topElement())
            index2 = closing.index(string[i])
            if(index1==index2):
                s.pop()
            else:
                return False
    if(s.size==0):
        return True
    else:
        return False

string = input()
print("The given string has balanced paranthesis: ",isBalParenthesis(string))