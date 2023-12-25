def symm(matrix):
    transpose = [[matrix[row][col] for row in range(len(matrix))]for col in range(len(matrix))]
    for i in range(len(matrix)):
        if matrix[i] != transpose[i]:
            return False
        return True

matrix = [[1,2,3], [2,4,5],[3,5,6]]
for i in matrix:
    print(i)
print()
print(symm(matrix))