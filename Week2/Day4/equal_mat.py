def max_matrix(matrix1,matrix2):
    if matrix1 == matrix2:
        return True
    return False


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
matrix2 = [[1, 2, 2], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print(max_matrix(matrix1,matrix2))