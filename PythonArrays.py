from array import *

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