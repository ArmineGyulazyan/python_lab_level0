def count_Ms(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            count = 0
            if matrix[row][col] == 0:
                if row != 0 or col != 0:
                    s_row = row - 1 if row - 1 >= 0 else row
                    e_row = row + 2 if row + 2 <= len(matrix) else len(matrix)
                    s_col = col - 1 if col - 1 >= 0 else col
                    e_col = col + 2 if col + 2 <= len(matrix[0]) else len(matrix[0])
                    for i in range(s_row,e_row):
                        for j in range(s_col,e_col):
                            if matrix[i][j] == 'M' and i < len(matrix) and j < len(matrix[0]):
                                count += 1
                    matrix[row][col] = count
                else:
                    for i in range(row,row+2):
                        for j in range(col,col+2):
                            if matrix[i][j] == 'M' and i < len(matrix) and j < len(matrix[0]):
                                count += 1
                    matrix[row][col] = count

    return matrix

matrix = [[0,'M',0,'M',0],
          [0, 0,'M',0, 0],
          [0, 0, 0, 0, 0],
          ['M','M',0,0,0],
          [ 0, 0, 0,'M',0]]
count_Ms(matrix)
for i in matrix:
    print(i)