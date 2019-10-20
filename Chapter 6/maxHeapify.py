#maintaining heap property


def MAX_HEAPIFY(arr, i):
    heapSize = len(arr)
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left <= heapSize and arr[left] > arr[i]:
        largest = left
    if right <= heapSize and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        MAX_HEAPIFY(arr, largest)


arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
MAX_HEAPIFY(arr, 1)
print(arr)
