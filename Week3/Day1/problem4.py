def divisors(n):
    divs = [i for i in range(1,n) if n % i == 0]
    return sum(divs)

print(divisors(6))