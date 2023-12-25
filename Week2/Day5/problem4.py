mat = [[0, 1, 0, 1, 1, 0],
       [0, 0, 0, 1, 1, 0],
       [1, 1, 1, 0, 0, 0],
       [1, 1, 0, 0, 1, 0],
       [0, 0, 0, 1, 1, 1],
       [0, 0, 0, 1, 0, 0]]

def DFS(mat, row, col, index_row, index_col):
    row, col = len(mat), len(mat[0])
    if mat[index_row][index_col] == 0:
        return
    mat[index_row][index_col] = 0
    if index_row != 0:
        DFS(mat, row, col, index_row-1, index_col)
    if index_row != row - 1:
        DFS(mat, row, col, index_row+1, index_col)
    if index_col != 0:
        DFS(mat, row, col, index_row, index_col-1)
    if index_col != col - 1:
        DFS(mat, row, col, index_row, index_col+1)


def islands(mat):
    counter = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                DFS(mat, len(mat), len(mat[0]), i, j)
                counter += 1
    return counter


print(islands(mat))