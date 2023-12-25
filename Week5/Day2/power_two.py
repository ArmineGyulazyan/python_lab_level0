def pow_two(n):
    return n>0 and n&(n-1)==0

print(pow_two(16))
print(pow_two(132))
print(pow_two(32))
