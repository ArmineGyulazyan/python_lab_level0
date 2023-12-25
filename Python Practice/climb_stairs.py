def climbStairs(n):
    first, sec = 1, 1
    for i in range(2, n + 1):
        first, sec = sec, first + sec
    return sec

print(climbStairs(44))