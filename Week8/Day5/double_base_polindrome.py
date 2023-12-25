def is_polindrome(n):
    return str(n) == str(n)[::-1]

def to_bin(n):
    st = ''
    while n > 0:
        st += str(n%2)
        n //= 2
    return st[::-1]

s = 0
for i in range(1000000):
    if is_polindrome(i):
        if is_polindrome(to_bin(i)):
            s+=i
print(s)