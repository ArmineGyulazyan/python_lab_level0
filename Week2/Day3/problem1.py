matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col],end=" ")
    print()

#print([[matrix[row][col] for col in range(len(matrix(row)))]for row in range(len(matrix))])
#print(mat)