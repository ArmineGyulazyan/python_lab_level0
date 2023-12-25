def rev_bit(n):
    if n == 0:
        return 0
    st_bin = ''
    while n > 0:
        st_bin = str(n % 2)+st_bin
        n //=  2

    return st_bin[::-1]


print(rev_bit(252))

