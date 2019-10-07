#merge sort


def merge(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    left = list()
    right = list()
    for i in range(n1):
        left.append(arr[start + i])
    for j in range(n2):
        right.append(arr[mid + j + 1])
    left.append(2147483647)
    right.append(2147483647)
    i = 0
    j = 0
    for k in range(start, end + 1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid + 1, end)
        merge(arr, start, mid, end)
        return arr


arr = [0, 7, 8, 5, 4, 9, 2, 22]
print('Sorted array:', mergeSort(arr, 0, len(arr) - 1))