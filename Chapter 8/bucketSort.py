#bucket sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j > -1 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucketSort(arr):
    newArr = [[] for i in range(10)]
    for each in arr:
        indx = int(each * 10)
        newArr[indx].append(each)
    for each in newArr:
        insertionSort(each)
    result = list()
    for i in range(10):
        for j in range(len(newArr[i])):
            result.append(newArr[i][j])
    print('Sorted array:', result)


def main():
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    bucketSort(arr)


main()