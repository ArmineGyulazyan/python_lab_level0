def check_min_crov(mat,i):
    return min([x[i] for x in mat])

def check_max_line(mat,i):
    return max(mat[i])

def tamb(mat):
    d = {}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == check_max_line(mat,i) and mat[i][j] == check_min_crov(mat,j):
                d[mat[i][j]] = (i,j)
    return d
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(tamb(matrix))