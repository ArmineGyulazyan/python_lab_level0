def hammingDistance(self, x, y):
    num = x ^ y
    count = 0
    while num != 0:
        if num % 2 == 1:
            count += 1
        num //= 2
    return count