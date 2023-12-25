def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

sum_p = 0
for i in range(1000000,2000000):
    if is_prime(i):
        sum_p += i
print(sum_p)