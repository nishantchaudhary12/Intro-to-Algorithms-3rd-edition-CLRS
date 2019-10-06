#insertion sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j > -1 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [0, 7, 8, 5, 4, 9, 2, 22]
print('Sorted array:', insertionSort(arr))