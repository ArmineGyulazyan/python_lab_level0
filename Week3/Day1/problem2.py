def perfect_num(n):
    lsc = [i for i in range(1,n) if n % i == 0]
    return True if sum(lsc) == n else False

print(perfect_num(6))
print(perfect_num(496))
print(perfect_num(55))
