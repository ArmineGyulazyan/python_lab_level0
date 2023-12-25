def large_prime_fact(n):
    max_p = 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 and is_prime(i):
            max_p = i
    return max_p

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

print(large_prime_fact(600851475143))