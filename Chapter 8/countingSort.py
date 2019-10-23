#counting sort


def countingSort(arr, k):
    c = [0 for i in range(k + 1)]

    for each in arr:
        c[each] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    sortedArr = [0 for i in range(len(arr))]


    for j in range(len(arr) - 1, -1, -1):

        sortedArr[c[arr[j]] - 1] = arr[j]
        c[arr[j]] -= 1

    return sortedArr


def main():
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    print(arr)
    k = 5
    print('Sorted array:', countingSort(arr, k))


main()