class DisjointSet():
    def __init__(self, elements):
        self.cnt = elements
        self.parent = [i for i in range(0,elements)]
        self.rank = [0 for i in range(0,elements)]
    
    def find(self, ele):
        if(self.parent[ele]==ele):
            return ele
        self.parent[ele] = self.find(self.parent[ele])
        return self.parent[ele]
    
    def union(self, ele1, ele2):
        rep1 = self.find(ele1)
        rep2 = self.find(ele2)
        if(rep1==rep2):
            return
        if(self.rank[rep1]==self.rank[rep2]):
            self.rank[rep1]+=1
            self.parent[rep2] = rep1
        elif(self.rank[rep1]>self.rank[rep2]):
            self.parent[rep2] = rep1
        else:
            self.parent[rep1] = rep2 
