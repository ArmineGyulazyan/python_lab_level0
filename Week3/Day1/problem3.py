def transpose(matrix):
    ls_t = [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix))]
    return ls_t


matrix = [[i + j for j in range(1,4)] for i in range(0,8,3)]
for i in matrix:
    print(i)
print()
for i in transpose(matrix):
    print(i)
