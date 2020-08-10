from collections import deque

def SubarrMaxElement(arr, k):
    n=len(arr)
    dq = deque()
    ans=[]
    for i in range(k):
        while dq and arr[dq[-1]]<=arr[i]:
            dq.pop()
        dq.append(i)
    for i in range(k,n):
        ans.append(arr[dq[0]])
        while dq and i-dq[0]>=k:
            dq.popleft()
        while dq and arr[dq[-1]]<=arr[i]:
            dq.pop()
        dq.append(i)
    ans.append(arr[dq[0]])
    return ans
        
arr = list(map(int, input("Enter Array: ").split()))
k = int(input("Enter k: "))

print(SubarrMaxElement(arr,k))