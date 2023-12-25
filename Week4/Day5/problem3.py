def mat_product(mat1,mat2):
    mat3 = [[0 for _ in range(len(mat1))]for _ in range(len(mat1))]

    for i in range(len(mat3)): #0
        for j in range(len(mat3)): #0
            sum_e = 0
            for k in range(len(mat3)): #0
                sum_e += (mat1[i][k]*mat2[k][j])
                mat3[i][j] = sum_e
    return mat3


mat1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]
mat2 = [[3,4,5],
        [6,7,8],
        [9,10,11]]

for i in mat_product(mat1,mat2):
    print(i)
# 5 5
# 3 3