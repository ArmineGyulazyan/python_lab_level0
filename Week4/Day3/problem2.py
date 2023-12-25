def logarithm_2base(n):
    '''
    base = 2
    count = 0
    while n != 1:
        if n % base == 0:
            n /= base  # 4,2,1
            count += 1
    return count
    '''
    if n>0 and n < 1:
        exp = -0.1
        while 2**exp-n > 0.000000000001:
            exp = exp - 0.1
        return exp
    exp = 0
    while n-2**exp > 0.00000000000000000001: #7
        exp += 0.1  #0.1
    return exp

print(logarithm_2base(8))
print(logarithm_2base(32))
print(logarithm_2base(15))
print(logarithm_2base(0.125))





