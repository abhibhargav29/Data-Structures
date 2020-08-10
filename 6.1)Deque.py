from collections import deque

#Takes array and k and returns answer array.
def SubarrMaxElement(arr, k):
    n=len(arr)
    #This deque created will hold the necessary elements an the leftmost element will always be the maximum.
    dq = deque()
    ans=[]
    #Iteration fo starting k elements.
    for i in range(k):
        while dq and arr[dq[-1]]<=arr[i]:
            dq.pop()
        dq.append(i)
    #Iteration for remaining k elements.
    for i in range(k,n):
        ans.append(arr[dq[0]])
        while dq and i-dq[0]>=k:
            dq.popleft()
        while dq and arr[dq[-1]]<=arr[i]:
            dq.pop()
        dq.append(i)
    ans.append(arr[dq[0]])
    return ans

#Driver Code
arr = list(map(int, input("Enter Array: ").split()))
k = int(input("Enter k: "))
print(SubarrMaxElement(arr,k))
