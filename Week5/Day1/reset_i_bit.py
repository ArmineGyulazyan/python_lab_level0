def reset_i_bit(n,i):
    ch_bit = ~(1<<i)
    res = n&ch_bit
    return res

print(reset_i_bit(4,4))