#the maximum subarray problem
#divide and conquer


def findMaximumCrossSubarray(arr, low, mid, high):
    leftSum = -2147483647
    currSum = 0
    maxLeft = 0
    for i in range(mid, low-1, -1):
        currSum += arr[i]
        if currSum > leftSum:
            leftSum = currSum
            maxLeft = i
    rightSum = -2147483647
    currSum = 0
    maxRight = 0
    for i in range(mid + 1, high+1):
        currSum += arr[i]
        if currSum > rightSum:
            rightSum = currSum
            maxRight = i + 1
    return maxLeft, maxRight, leftSum + rightSum


def findMaximumSubarray(arr, low, high):
    if high == low:
        return low, high, arr[low]
    else:
        mid = (low + high)//2
        leftLow, leftHigh,  leftSum = findMaximumSubarray(arr, low, mid)
        rightLow, rightHigh, rightSum = findMaximumSubarray(arr, mid + 1, high)
        crossLow, crossHigh, crossSum = findMaximumCrossSubarray(arr, low, mid, high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return leftLow, leftHigh, leftSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            return rightLow, rightHigh, rightSum
        else:
            return crossLow, crossHigh, crossSum


arr = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
diffArr = list()
for i in range(len(arr)-1):
    diffArr.append(arr[i+1] - arr[i])
buy, sell, profit = findMaximumSubarray(diffArr, 0, len(diffArr)-1)
print('Best day to buy stocks after day:', buy, 'To make maximum profit sell it after:', sell, 'day.', 'Profit made:', profit)