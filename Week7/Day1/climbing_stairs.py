def climbStairs(self, n):
    prev, sec = 1, 1
    for _ in range(2, n + 1):
        prev, sec = sec, prev + sec
    return sec