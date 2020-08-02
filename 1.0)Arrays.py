from array import *

#Binary Search
def BinarySearch(a, val):
    n=len(a)
    if(n==1):
        if(a[0]==val):
            return 0
        else:
            return -1
    mid=n//2
    if(a[mid]==val):
        return mid
    elif(a[mid]>val):
        return BinarySearch(a[:mid],val)
    else:
        return BinarySearch(a[mid+1:],val)+mid+1

#Array Manipulation
#The function taes in an integer n and creates 0 array of size n, the perform the queries one by one.
#The queries is a list of 3-tuples, the first two tell us indexes(from 1) and third number is the number to add.
#Ex- for a querry  1 5 6, we will add 6 to every number from 1 to 5 index(both inclusive).
#The function returns max element in array after performing all the querries.
#The function is not called in driver code.
def arrayManipulation(n, queries):
    arr=[0]*(n)
    for q in queries:
        arr[q[0]-1]+=q[2]
        if(q[1]<n):
            arr[q[1]]-=q[2]
    maxElement=0
    x=0
    for i in range(len(arr)):
        x=x+arr[i]
        if(x>maxElement):
            maxElement=x
    return maxElement

def rotate(arr, n, d):
    d=d%n
    GCD = gcd(n,d)
    for i in range(GCD):
        temp = arr[i]
        j=i
        while(True):
            k=j+d
            if(k>=n):
                k= k-n
            if(k==i):
                break
            arr[j]=arr[k]
            j=k
        arr[j]=temp
    print(" ".join(map(str, arr)))

#Driver code
r=list(map(int, input("Initialize the array with some elements: ").split()))
arr = array("i", r)
print("\n")

print("INDEX:"+\
        "\n\"+\" -> Add element"+\
        "\n\"-\" -> Delete element"\
        "\n\"s\" -> Search element"\
        "\n\"d\" -> Display Array"\
        "\n\"e\" -> Exit")
print("\n")

#The menu
while(True):
    x = input("Enter Your choice: ")
    if(x=="e"):
        break
    elif(x=="+"):
        ele= int(input("Enter element: "))
        pos= int(input("Enter position: "))
        arr.insert(pos, ele)
        print("Inserted")
        continue
    elif(x=="-"):
        ele= int(input("Enter element: "))
        arr.remove(ele)
        print("Deleted")
        continue
    elif(x=="d"):
        for ele in arr:
            print(ele, end=" ")
        print()
        continue
    elif(x=="s"):
        ele = int(input("Enter element: "))
        x = BinarySearch(arr,ele)
        if(x!=-1):
            print(ele,"found at:", x)
        else:
            print("Not Found")
        continue
    else:
        pass

print("GoodBye")
