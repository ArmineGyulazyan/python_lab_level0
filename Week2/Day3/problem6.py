def up_sec_diagonal_change(matrix):
    #with 1 loop
    for row in range(len(matrix)):
        matrix[row][row],matrix[row][(len(matrix)-1)-row] = matrix[row][(len(matrix)-1)-row],matrix[row][row]

    return matrix
    '''
    #with 2 loops
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                tmp = matrix[row][col]
                matrix[row][col] = matrix[row][(len(matrix[0])-1)-row]
                matrix[row][(len(matrix[0])-1)-row] = tmp
    return matrix
    '''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
up_sec_diagonal_change(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()


'''
1, 2, 3    3 2 1            
4, 5, 6    4 5 6           
7, 8, 9    9 8 7
'''