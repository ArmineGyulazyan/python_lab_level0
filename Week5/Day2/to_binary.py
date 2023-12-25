def to_bin(n):
    if n == 0:
        return 0
    st_bin = ''
    while n > 0:
        st_bin = str(n % 2)+st_bin
        n //=  2

    return st_bin

print(to_bin(7))
print(to_bin(0))
print(to_bin(252))
