#heap sort

def HEAPSORT(arr):
    heapSize = len(arr)
    BUILD_MAX_HEAP(arr, heapSize)
    for i in range(len(arr) - 1, 0, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        heapSize = heapSize - 1
        MAX_HEAPIFY(arr, 0, heapSize)


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
HEAPSORT(arr)
print('Sorted Array:', arr)
