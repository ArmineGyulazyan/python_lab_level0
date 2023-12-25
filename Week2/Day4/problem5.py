def up_sec_list(matrix):
    sum_d = 0
    for row in range(len(matrix)-1):
        for col in range((len(matrix)-1)-row):
            sum_d += matrix[row][col]

    return sum_d


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(up_sec_list(matrix))
