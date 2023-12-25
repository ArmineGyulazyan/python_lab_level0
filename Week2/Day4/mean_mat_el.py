def max_matrix(matrix):
    sum_e = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            sum_e += matrix[row][col]
    return sum_e/(len(matrix)*len(matrix[0]))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(matrix)
print(max_matrix(matrix))