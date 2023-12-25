def is_prime(n):
    primes = [i for i in range(2,n+1)
              if all(i%j for j in range(2,int(i**0.5)+1))]
    return primes

print(is_prime(10))
print(is_prime(20))
print(is_prime(100))
print([i for i in range(2,10) if all(i%j for j in range(2,int(i**0.5)+1))])