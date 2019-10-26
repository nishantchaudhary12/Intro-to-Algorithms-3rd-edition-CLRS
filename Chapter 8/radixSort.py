# radix sort

def countingSort(arr, exp):
    n = len(arr)
    result = [0 for i in range(n)]
    count = [0 for i in range(10)]

    for i in range(n):
        indx = arr[i] // exp
        count[indx % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        indx = arr[i] // exp
        result[count[indx % 10] - 1] = arr[i]
        count[indx % 10] -= 1

    for i in range(n):
        arr[i] = result[i]


def radixSort(arr):
    k = max(arr)
    exp = 1
    while k//exp > 0:
        countingSort(arr, exp)
        exp *= 10

    print('Sorted Array:', arr)


def main():
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    radixSort(arr)


main()
