def flip(n,i):
    ch_bit = 1<<i
    res = n^ch_bit
    return res

print(flip(7,6))
