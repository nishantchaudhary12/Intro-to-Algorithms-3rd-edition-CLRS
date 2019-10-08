#the maximum subarray problem
#brute force approach

def maximumSubarray(arr):
    profit = 0
    buy, sell = -1, -1
    for i in range(len(arr)-1):
        j = i + 1
        while j < len(arr):
            curr = arr[j] - arr[i]
            if profit < curr:
                profit = curr
                buy = i
                sell = j
            j += 1
    return buy, sell

arr = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
buy, sell = maximumSubarray(arr)
print('Best day to buy stocks after day:', buy, 'To make maximum profit sell it after:', sell, 'day')