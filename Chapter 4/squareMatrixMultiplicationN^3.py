#matrix multiplication
#n^3 solution

def squareMatrixMultiplication(matrix_1, matrix_2):
    n = len(matrix_1)
    result = [[] for i in range(n)]
    for i in range(n):
        k = 0
        while k < n:
            curr = 0
            j = 0
            while j < n:
                curr += (matrix_1[i][j] * matrix_2[j][k])
                j += 1
            k += 1
            result[i].append(curr)
    return result


matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(squareMatrixMultiplication(matrix_1, matrix_2))