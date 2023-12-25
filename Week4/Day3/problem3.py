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

print(log_anybase(8,2))
print(log_anybase(9,3))
print(log_anybase(64,4))
#print(log_anybase(8,0.5))
print(log_anybase(0.5,2))



