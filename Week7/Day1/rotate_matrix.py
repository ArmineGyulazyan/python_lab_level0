def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
            matrix[i].reverse()
    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

