def armstrong(num):
    sum = 0
    n = len(str(num))
    original = num
    while num != 0:
        dig = num % 10
        sum += (dig**n)
        num //= 10
    if sum == original:
        return 'YES'
    return 'NO'

print(armstrong(153))
print(armstrong(155))
print(armstrong(407))


