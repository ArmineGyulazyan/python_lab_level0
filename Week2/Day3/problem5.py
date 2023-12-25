def up_main_diagonal(matrix):
    sum = 0
    for row in range(len(matrix)):
        for col in range(row,len(matrix)):
           sum += matrix[row][col]
    return sum

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(up_main_diagonal(matrix))
