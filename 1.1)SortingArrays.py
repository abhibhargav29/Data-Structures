def BubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
def SelectionSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if(arr[j]<arr[i]):
                arr[j], arr[i] = arr[i], arr[j]
    
def InsertionSort(arr):
    n=len(arr)
    for i in range(n):
        k=arr[i]
        j=i-1
        while(j>=0 and arr[j]>k):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=k

def MergeSort(arr):
    n=len(arr)
    mid=n//2
    if(n<=1):
        return arr
 
    left_list  = MergeSort(arr[:mid])
    right_list = MergeSort(arr[mid:])
    return merge(left_list, right_list)

#Helper
def merge(left, right):
    m=len(left)
    n=len(right)
    new=[]
    j=0
    k=0
    while(j<m and k<n):
        if(left[j]<=right[k]):
            new.append(left[j])
            j+=1
        else:
            new.append(right[k])
            k+=1
    if(j<m):
        new.extend(left[j:])
    else:
        new.extend(right[k:])
    return new

def QuickSort(arr, low, high):
    if(low<high):
        p=partition(arr,low,high)

        QuickSort(arr,low,p-1)
        QuickSort(arr,p+1,high)

#Helper
def partition(arr, low, high):
    i = ( low-1 )          
    pivot = arr[high]     
  
    for j in range(low , high):   
        if   arr[j] < pivot:  
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )

    
#Driver Code
arr = list(map(int, input().split()))
QuickSort(arr,0,len(arr)-1)
print(arr)
