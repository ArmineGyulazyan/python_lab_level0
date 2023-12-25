def magic_matrix(matrix):
    rows = [sum(i) for i in matrix]
    cols = [sum(i[0::]) for i in matrix]
    main_diag = sum([matrix[i][i] for i in range(len(matrix))])
    sec_diag = sum([matrix[i][j] for j in range(len(matrix)) for i in range(len(matrix)) if i + j == (len(matrix[0]) - 1)])

    if main_diag not in rows or main_diag not in cols or main_diag != sec_diag:
        return 'NO MAGIC'
    if sec_diag not in rows or sec_diag not in cols:
        return 'NO MAGIC'
    if not all(rows[i]==cols[i] for i in range(len(rows))):
        return 'NO MAGIC'
    return 'YES'

mat1 = [[1,2,1],[2,2,0],[3,1,0]]
print(magic_matrix(mat1))

#another version
'''
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row
    target_sum = sum(matrix[0])
    
    # Check the sums of rows
    for row in matrix:
        if sum(row) != target_sum:
            return False
    
    # Check the sums of columns
    for col in range(n):
        col_sum = sum(matrix[row][col] for row in range(n))
        if col_sum != target_sum:
            return False
    
    # Check the sum of the main diagonal (top-left to bottom-right)
    diag1_sum = sum(matrix[i][i] for i in range(n))
    if diag1_sum != target_sum:
        return False
    
    # Check the sum of the secondary diagonal (top-right to bottom-left)
    diag2_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    if diag2_sum != target_sum:
        return False
    
    return True

# Test cases
matrix1 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
matrix2 = [[2, 7, 6], [9, 5, 1], [4, 1, 8]]

print(is_magic_square(matrix1))  # True (a magic square)
print(is_magic_square(matrix2))  # False (not a magic square)

'''