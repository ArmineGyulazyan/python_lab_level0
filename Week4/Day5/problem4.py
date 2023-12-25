def matrix_det(matrix):
    mul1 = 1
    mul2 = 1
    for i in range(len(matrix)):
        mul1 *= matrix[i][i]
        for j in range(len(matrix)):
            if i + j == len(matrix[0]) - 1:
                mul2 *= matrix[i][j]

    return mul1-mul2


mat1 = [[1,2],
        [4,5]]
print(matrix_det(mat1))