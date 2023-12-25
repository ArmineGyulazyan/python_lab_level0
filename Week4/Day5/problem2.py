def third_sum(mat1,mat2):
    mat3 = [[mat1[i][j]+mat2[i][j] for j in range(len(mat1))]for i in range(len(mat1))]
    return mat3

mat1 = [[1,2,3], [2,4,5],[3,5,6]]
mat2 = [[1,1,1], [2,2,2],[3,3,3]]
for i in third_sum(mat1,mat2):
    print(i)