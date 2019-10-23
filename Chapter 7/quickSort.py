#quick sort


def quickSort(arr, start, end):
    if start < end:
        key = partition(arr, start, end)
        quickSort(arr, start, key - 1)
        quickSort(arr, key + 1, end)


def partition(arr, start, end):
    x = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= x:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    arr[end] = arr[i + 1]
    arr[i + 1] = x
    return i + 1




def main():
    arr = [2, 8, 7, 1, 3, 5, 6]
    quickSort(arr, 0, len(arr) - 1)
    print(arr)
    print('Sorted array:', arr)


main()