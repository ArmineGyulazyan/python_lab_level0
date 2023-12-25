def swap(n,i,j):
    sw_i = (n>>i)&1
    sw_j = (n>>j)&1

    if sw_i != sw_j:
        n ^= (1<<i)
        n ^= (1<<j)


    return n

print(swap(10,6,4))