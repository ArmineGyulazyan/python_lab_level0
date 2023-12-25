def matrix_rotate(matrix):
    for row in range(len(matrix)//2):
        matrix[row], matrix[(len(matrix)-1)-row][::-1] = matrix[(len(matrix)-1)-row][::-1], matrix[row]
    return matrix

matrix = [[1,2,3],
       [4,5,6],
       [7,8,9]]

matrix_rotate(matrix)
for i in matrix:
    print(i)