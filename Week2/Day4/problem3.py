def max_row_list(matrix):
    tmp = matrix[0][0]
    ls = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] >= tmp:
                tmp = matrix[row][col]
        ls.append(tmp)

    return ls

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(matrix)
print(max_row_list(matrix))