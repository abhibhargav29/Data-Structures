from math import factorial
from collections import Counter

#Finds Lexicographic rank.
#Works for strings with only upper or smaller case non repeating letters.
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

#This function takes in a string and returns "YES" if all the elements 
#occur same number of times or we can delete just one element to make it valid
def isValid(s):
    d = Counter(Counter(s).values())
    print(d)
    if(len(d)==1):
        return "YES"
    elif(len(d)>2):
        return "NO"
    k1,k2=d.keys()
    v1,v2=d.values()
    if(min(v1,v2)==1):
        if(abs(k1-k2)==1):
            return "YES"
        elif(min(k1,k2)==1):
            if(d[1]==1):
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
    else:
        return "NO"

string = input()
print(LexicographicRank(string))
print(isValid(s))
