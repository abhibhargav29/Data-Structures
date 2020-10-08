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

#helper for longest palindrome
def aroundCenter(s, L, R):
    right= R
    left = L
    while((left>=0 and right<len(s))):
        if(s[right]==s[left]):
            right+=1
            left-=1
        else:
            break
    return right-left-1

#Returns longest substring that is palindrome
#Not called in driver code
def longestPalindrome(s):
    if(s == None or len(s)==0):
        return ""
    n = len(s)
    finalStart=0
    finalEnd=0
    for i in range(n):
        len1 = aroundCenter(s,i,i)
        len2 = aroundCenter(s,i,i+1)
        length = max(len1,len2)
        if(length>finalEnd-finalStart):
            finalStart = i-(length-1)//2
            finalEnd = i+(length//2)
    return s[finalStart:finalEnd+1]

s = input()
print(longestPalindrome(s))    
    
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
    if(Deletions==len(a)+len(b)):
        return -1
    else:
        return Deletions

#This function finds the longest common subsequence in two strings
#A subsequence is NOT EXACTLY like a substring as it may or may not be continuous.
#Any string is a child(subsequence) of a parent string if it can be formed from the parent string by 0 or more character deletions.
#Example- "ACD" is the longest subsequence of "ABCD" and "AGCTD".
#The function has not been called in driver code
def commonChild(s1, s2):
    m=len(s1)
    n=len(s2)
    #We use this matrix as tabulation for this DP approach.
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

#Rabin Karp algo to find pattern in a string
#The function has not been called in the driver code
def RabinKarp(string, pat):
    res=[]
    
    patHashVal  = 0
    currHashVal = 0 
    for i in range(len(pat)):
        patHashVal+=ord(pat[i])
        currHashVal+= ord(string[i])
    
    for j in range(0,len(string)-len(pat)+1):
        if(patHashVal==currHashVal):
            flag=0
            for k in range(len(pat)):
                if(pat[k]!=string[j+k]):
                    flag=1
                    break
            if(flag==0):
                res.append(j)
        currHashVal-= ord(string[j])
        if(j+len(pat)<len(string)):
            currHashVal+= ord(string[j+len(pat)])
    return " ".join(map(str, res))

#helper for KMP Algo to make LPS array
def computeLPS(string, m):
    LPSarr=[0]*m
    L=0
    i=1
    while(i<m):
        if(string[i]==string[L]):
            L+=1
            LPSarr[i]=L
            i+=1
        else:
            if(L!=0):
                #Change L but not i
                L=LPSarr[L-1]
            else:
                LPSarr[i]=0
                i+=1
    return LPSarr

#KMP algo to find a pat in a string.
#The function has not been called in the driver code.
def KMP(string, pat):
    n=len(string)
    m=len(pat)
    #Get the lps array
    lps = computeLPS(pat, m)
    
    i=0
    j=0
    Found=[]
    #Use lps array to find the next j to match from.
    while(i<n):
        while(j<m and i<n and string[i]==pat[j]):
            i+=1
            j+=1
        if(j==len(pat)):
            Found.append(i-len(pat))
            j=lps[j-1]
        elif(i<n and string[i] != pat[j]):
            if(j!=0):
                j=lps[j-1]
            else:
                i+=1
    return " ".join(map(str, Found))

#A function that takes a gene and returns the length of the smallest substring that is needed
#to be replaced to make occurence of every letter(A,C,G,T) equal to length/4.
#It is assumed that the length of gene passed is a multiple of 4.
#The function is not called in driver code
def steadyGene(gene):
    #Dictionary to store count
    dic = {'A':0,'T':0,'C':0,'G':0}
    for i in gene:
        dic[i]+=1
    x=len(gene)
    factor=x/4

    if dic['A']==factor and dic['T']==factor and dic['C']==factor and dic['G']==factor:
        return 0
    #upper will traverse to take care of every letter occuring more number of times.
    #lower will traverse for letters that are less number of times.
    upper=0
    lower=0
    minlen=x
    while upper<x and lower<x:
        while (dic['A']>factor or dic['C']>factor or dic['T']>factor or\
        dic['G']>factor) and upper<x:
            dic[gene[upper]]-=1
            upper+=1
        while dic['A']<=factor and dic['C']<=factor and dic['T']<=factor\
        and dic['G']<=factor:
            dic[gene[lower]]+=1
            lower+=1
        if upper - lower < minlen :
            minlen=upper-lower+1
    return minlen

#Driver Code
string = input()
print(LexicographicRank(string))
print(isValid(string))
print(specialSubstrCount(string))
