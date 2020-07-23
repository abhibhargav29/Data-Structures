from math import factorial
from collections import Counter

#Finds Lexicographic rank.
#Works for strings with only upper or smaller case non repeating letters.
def LexicographicRank(s):
    n = len(s)
    rank=1
    for i in range(n):
        mul=0                  #Number of letters that come before ith letter of s
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

#This function counts number of special sub strings in a string
#Special substrings are either strings with same character like "a", "aaaa", "bbbb" etc or only the middle element is different in case of odd length strings.
#Ex- For aabaab the list of special Substrings will be {"a", "a", "b", "a", "a", "b", "aa", "aa", "aabaa", "aba"}
def specialSubstrCount(n, s):
    TotalCount=0
    #Array that will for each char contain how many characters repeat consecutevely for it.
    sameChar=[0]*n
    i=0
    #For the even length strings
    while(i<n):
        sameCharCount=1
        j=i+1
        while(j<n and s[j]==s[i]):
            j+=1
            sameCharCount+=1
        TotalCount+=int((sameCharCount*(sameCharCount+1))/2)
        sameChar[i]=sameCharCount
        i=j
    #For odd length strings
    for k in range(1,n):
        if(s[k]==s[k-1]):
            sameChar[k]=sameChar[k-1]
        if(k<n-1):
            if(s[k-1]==s[k+1] and s[k]!=s[k-1]):
                TotalCount+= min(sameChar[k-1],sameChar[k+1])
    return TotalCount    
    
#Function that returns min number of deletions to make two strings anagrams.
#The function has not been called in driver code
def makeAnagram(a, b):
    a=Counter(a)
    b=Counter(b)
    Deletions=0
    for k in a.keys():
        if(k not in b.keys()):
            Deletions+=a[k]
        else:
            Deletions+=abs(a[k]-b[k])
            del b[k]
    for k in b.keys():
        Deletions+=b[k]
    return Deletions

#This function finds the longest common subsequence in two strings
#A subsequence is NOT EXACTLY like a substring as it may or may not be continuous.
#Any string is a child(subsequence) of a parent string if it can be formed from the parent string by 0 or more character deletions.
#Example- "ACD" is the longest subsequence of "ABCD" and "AGCTD".
def commonChild(s1, s2):
    m=len(s1)
    n=len(s2)
    Matrix=[[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                Matrix[i][j]=0
            elif(s1[i-1]==s2[j-1]):
                Matrix[i][j] = 1+Matrix[i-1][j-1]
            else:
                Matrix[i][j] = max(Matrix[i-1][j], Matrix[i][j-1])
    return Matrix[m][n]

#Driver Code
string = input()
print(LexicographicRank(string))
print(isValid(string))
print(specialSubstrCount(string))
