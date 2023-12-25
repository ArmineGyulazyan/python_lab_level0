def max_matrix(matrix):
    tmp = matrix[0][0]
    for row in range(1,len(matrix)):
        for col in range(1,len(matrix[0])):
            if matrix[row][col] >= tmp:
                tmp = matrix[row][col]
                max_ind = (row,col)
    return tmp, max_ind


matrix = [[1, 2, 3], [4, 24, 6], [7, 8, 9], [10, 11, 12]]
print(matrix)
print(max_matrix(matrix))