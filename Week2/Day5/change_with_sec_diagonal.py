def ch_with_sec_diagonal(matrix):
    for row in range(len(matrix)-1):
        for col in range(len(matrix)-1-row):

                matrix[row][col], matrix[len(matrix)-1-col][len(matrix)-1-row] = matrix[len(matrix)-1-col][len(matrix)-1-row], matrix[row][col]
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in ch_with_sec_diagonal(matrix):
    print(i)
'''
1 2 3   
4 5 6
7 8 9
'''