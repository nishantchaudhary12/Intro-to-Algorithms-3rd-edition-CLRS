#priority queues
#heap maximum
#heap extract max
#heap increase key
#max heap insert

import sys

def HEAP_MAXIMUM(arr):
    return arr[0]


def HEAP_EXTRACT_MAX(arr):
    heapSize = len(arr)
    if heapSize < 1:
        return 'Heap underflow'
    maxElem = arr[0]
    arr[0] = arr[heapSize - 1]
    heapSize = heapSize - 1
    MAX_HEAPIFY(arr, 0, heapSize)
    return maxElem


def HEAP_INCREASE_KEY(arr, i ,key):
    if arr[i] > key:
        return 'New key is smaller than new key'
    arr[i] = key
    while i > 0 and arr[(i - 1)//2] < arr[i]:
        temp = arr[i]
        arr[i] = arr[(i - 1)//2]
        arr[(i - 1) // 2] = temp
        i = (i - 1)//2


def MAX_HEAP_INSERT(arr, key):
    arr.append(-sys.maxsize)
    HEAP_INCREASE_KEY(arr, len(arr) - 1, key)


def MAX_HEAPIFY(arr, i, heapSize):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heapSize and arr[left] > arr[i]:
        largest = left
    if right < heapSize and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        MAX_HEAPIFY(arr, largest, heapSize)


def BUILD_MAX_HEAP(arr, heapSize):
    for i in range(len(arr)//2, -1, -1):
        MAX_HEAPIFY(arr, i, heapSize)


arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
BUILD_MAX_HEAP(arr, len(arr))
print(arr)
print('Heap maximum:', HEAP_MAXIMUM(arr))
print('Heap extract max:', HEAP_EXTRACT_MAX(arr))
print(arr)
arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
HEAP_INCREASE_KEY(arr, 8, 15)
print(arr)
MAX_HEAP_INSERT(arr, 18)
print(arr)
