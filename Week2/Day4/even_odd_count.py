def max_matrix(matrix):
    ev = 0
    odd = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]%2==0:
                ev += 1
            else:
                odd +=1
    return ev,odd


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(matrix)
print(max_matrix(matrix))