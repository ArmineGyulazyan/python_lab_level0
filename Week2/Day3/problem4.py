def sec_diagonal_sum(matrix):
    sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if row+col == len(matrix)-1:
                sum += matrix[row][col]
    return sum

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

print(sec_diagonal_sum(matrix))
