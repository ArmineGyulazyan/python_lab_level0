with open('0081_matrix.txt','r') as filee:
    matrix = filee.read().splitlines(80)
    for t in range(len(matrix)):
        matrix[t] = matrix[t].split(',')

dp = [[0 for i in range(80)] for j in range(80)]
dp[0][0] = int(matrix[0][0])
for i in range(1, 80):
    dp[0][i] = int(matrix[0][i]) + dp[0][i - 1]
for i in range(1, 80):
    dp[i][0] = int(matrix[i][0]) + dp[i - 1][0]
for i in range(1, 80):
    for j in range(1, 80):
        dp[i][j] = int(matrix[i][j]) + min(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])