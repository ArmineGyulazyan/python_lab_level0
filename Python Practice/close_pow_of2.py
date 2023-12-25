def closest_pow_of2(n):
    if n>0 and n&(n-1) == 0:
        return log_anybase(n,2)

    return closest_pow_of2(n-1)

def log_anybase(n,base):
    if n>0 and n < 1:
        exp = -0.1
        while base**exp - n > 0.000000000001:
            exp -= 0.1
        return exp
    exp = 0
    while n - (base ** exp) > 0.000000000000001:  # 7
        exp += 0.1  # 0.1
    return exp

print(closest_pow_of2(17))
