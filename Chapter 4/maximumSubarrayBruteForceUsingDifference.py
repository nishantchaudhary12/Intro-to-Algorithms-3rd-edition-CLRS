#the maximum subarray problem
#working with diffrences (brute force)

def maximumSubarray(arr):
    buy, sell = -1, -1
    total = 0
    for i in range(len(arr)-1):
        j = i + 1
        currSum = arr[i]
        while j < len(arr):
            currSum += arr[j]
            if currSum > total:
                total = currSum
                buy = i
                sell = j + 1
            j += 1
    return buy, sell


arr = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
diffArr = list()
for i in range(len(arr)-1):
    diffArr.append(arr[i+1] - arr[i])
buy, sell = maximumSubarray(diffArr)
print('Best day to buy stocks after day:', buy, 'To make maximum profit sell it after:', sell, 'day')