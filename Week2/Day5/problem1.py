def row_to_col(matrix):

    for row in range(len(matrix)):
        for col in range(row,len(matrix[0])):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in row_to_col(matrix):
    print(i)
'''
1 2 3   
4 5 6
7 8 9
'''