def set_i_bit(n,i):
    ch_bit = 1 << i
    res = n | ch_bit
    return res

print(set_i_bit(4,4))