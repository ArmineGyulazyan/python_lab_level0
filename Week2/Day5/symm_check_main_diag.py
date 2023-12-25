def is_symmetric(matrix):

    # Check if the matrix is symmetric
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Test cases
matrix1 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matrix2 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 6, 7]
]

print(is_symmetric(matrix1))  # True (symmetric)
print(is_symmetric(matrix2))  # False (not symmetric)
