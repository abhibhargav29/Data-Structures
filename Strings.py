from math import factorial

def LexicographicRank(s):
    n = len(s)
    rank=1
    for i in range(n):
        mul=0
        for j in range(i+1,n):
            if(s[j]<s[i]):
                mul+=1
        rank+= mul*factorial(n-i-1)
    return rank

string = input()
print(LexicographicRank(string))
