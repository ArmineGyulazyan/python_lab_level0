def eventoZero(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row % 2 == 0:
                matrix[row][col] = 0
    return matrix


matrix = [[1, 2, 3],[4, 5, 6], [7, 8, 9],[10,11,12]]
print(eventoZero(matrix))