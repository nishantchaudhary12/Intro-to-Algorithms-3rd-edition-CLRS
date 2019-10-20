#building a heap

def MAX_HEAPIFY(arr, i):
    heapSize = len(arr)
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heapSize and arr[left] > arr[i]:
        largest = left
    # print(right)
    if right < heapSize and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        MAX_HEAPIFY(arr, largest)
    print(i)


def BUILD_MAX_HEAP(arr):
    heapSize = len(arr)
    for i in range(len(arr)//2, -1, -1):
        MAX_HEAPIFY(arr, i)


arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
BUILD_MAX_HEAP(arr)
print(arr)
