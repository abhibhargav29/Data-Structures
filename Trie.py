class TrieNode():
    def __init__(self):
        self.arr = [None]*26
        self.isEnd = False

class Trie():
    def __init__(self):
        self.head = TrieNode()

    def insert(self, string):
        curr = self.head
        n = len(string)
        i=0
        for letter in string:
            if(curr.arr[ord(letter)-ord("a")]==None):
                curr.arr[ord(letter)-ord("a")] = TrieNode()
                curr = curr.arr[ord(letter)-ord("a")]
                if(i==n-1):
                    curr.isEnd = True
                i+=1
            else:
                curr = curr.arr[ord(letter)-ord("a")]
                if(i==n-1):
                    curr.isEnd = True
                i+=1

    def delete(self, item, i=0, curr=None):
        if(curr==None):
            curr = self.head
        if(i==(len(item))):
            curr.isEnd = False
            if(self.isLeaf(curr)):
                del curr
                return None
            else:
                return curr
        curr.arr[ord(item[i])-ord("a")] = self.delete(item, i+1, curr.arr[ord(item[i])-ord("a")])
        if(self.isLeaf(curr)):
            del curr
            return None
        else:
            if(i!=0):
                return curr
        

    def isLeaf(self, node):
        for i in node.arr:
            if(i!=None):
                return False
        return True
    
    def search(self, item):
        n = len(item)
        curr = self.head
        for i in range(0, n):
            if(curr.arr[ord(item[i])-ord("a")]==None):
                return False
            else:
                curr = curr.arr[ord(item[i])-ord("a")]
        if(curr.isEnd==True):
            return True
        return False

    def printTrie(self, strings=[], curr = None):
        if(curr==None):
            curr = self.head
        if(curr.isEnd==True):
            print("".join(strings), end=" ")
        i=0
        for let in curr.arr:
            if(let==None):
                i+=1
                continue
            else:
                strings.append(chr(i+ord("a")))
                self.printTrie(strings, let)
                del strings[-1]
                i+=1

#driver code
strArr = ["bat", "cat", "but", "ans", "answer", "cut"]
t = Trie()
for string in strArr:
    t.insert(string)

print("Lexicographically printing trie: ", end="")
t.printTrie()
print()

t.delete("cat")
print("After deletion of cat:", end=" ")
t.printTrie()
print()

word = "cu"
if(t.search(word)):
    print(word,"is present")
else:
    print(word,"not present")