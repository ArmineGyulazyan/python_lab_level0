def ones_in_bin(num):
    count = 0
    while num > 0:
        count += num & 1
        num >>= 1
    return count

print(ones_in_bin(11))
