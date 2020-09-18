class KnapsackItems():
    def __init__(self, ind,  val, weight):
        self.wt = weight
        self.val  = val
        self.index = ind
        self.net = val/weight

def ActivitySelection(arr):
    arr = sorted(arr, key=lambda x: x[1])
    Ans = []
    Ans.append(arr[0])
    for ele in arr:
        if(ele[0]>=Ans[-1][1]):
            Ans.append(ele)
        else:
            pass
    print("These tasks would be performed:", Ans)

def FractionaKnapsack(Items, n):
    Items = sorted(Items, key = lambda x: x.net, reverse=True)
    Ans = []
    wt = 0
    finVal = 0
    for item in Items:
        if(item.wt<=n-wt):
            Ans.append(item.index)
            finVal += item.val 
            wt+=item.wt 
        else:
            finVal += item.net*(n-wt)
            Ans.append(item.index)
            break 
    print("Selected items:", Ans)
    print("Total value:", finVal)

#Activity selection
arr= [[1,2],[5,7],[8,9],[5,9],[0,6],[3,4]]
ActivitySelection(arr)

#Fractional Knapsack
I1 = KnapsackItems(1, 60, 10)
I2 = KnapsackItems(2, 40, 40)
I3 = KnapsackItems(3, 100, 20)
I4 = KnapsackItems(4, 120, 30)
cap = 50
arr = [I1, I2, I3, I4]
FractionaKnapsack(arr, cap)