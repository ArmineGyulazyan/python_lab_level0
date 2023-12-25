def diagonal_sum(matrix):
    sum = 0
    for row in range(len(matrix)):
        sum += matrix[row][row]
    return sum

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(diagonal_sum(matrix))
