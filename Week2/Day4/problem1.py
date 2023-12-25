def max_matrix(matrix):
    tmp = matrix[0][0]
    for row in range(1,len(matrix)):
        for col in range(1,len(matrix[0])):
            if matrix[row][col] >= tmp:
                tmp = matrix[row][col]
    return tmp


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(matrix)
print(max_matrix(matrix))