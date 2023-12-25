def down_sec_list(matrix):
    sum_d = 0
    for row in range(1,len(matrix)):
        for col in range(len(matrix)-row,len(matrix)):
            sum_d += matrix[row][col]

    return sum_d


matrix = [
    [1, 2, 3],
    [4,5,6],
    [7, 8, 9]]
for i in matrix:
    print(i)
print(down_sec_list(matrix))

