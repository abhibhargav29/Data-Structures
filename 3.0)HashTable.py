class ChainedHashTable():
    def __init__(self, m):
        self.Table= list([[] for i in range(m)])
        self.m = m

    def insert(self, num):
        key = num%(self.m)
        if(len(self.Table[key])<=5):
            self.Table[key].append(num)
        else:
            print("Chain length exeeded for",key,"key")

    def search(self, num):
        key=num%(self.m)
        for item in self.Table[key]:
            if(item==num):
                return True
        return False

    def delete(self, num):
        key=num%(self.m)
        for item in self.Table[key]:
            if(item==num):
                self.Table[key].remove(item)
                print(num,"deleted successfully.")
                return
        print("Item not present, can't be deleted.")

Lookup = ChainedHashTable(7)
arr = [3, 5, 4, 12, 14, 7, 8]
for item in arr:
    Lookup.insert(item)
print("Is 12 present:",Lookup.search(12))
print("Is 10 present:",Lookup.search(10))
Lookup.delete(12)
print("Is 12 present:",Lookup.search(12))
