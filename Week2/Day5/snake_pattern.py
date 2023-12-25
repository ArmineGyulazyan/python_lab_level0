def snake_matrix(n):
    #m = [[i+j for i in range(1,n+1)] for j in range(0,(n*n)-1,n)]
    #return m
    m = []
    for i in range(0, (n*n)-1, n):
        ls = []
        for j in range(1,n+1):
            ls.append(i+j)
        m.append(ls)

    for i1 in range(len(m)):
        if i1 % 2 != 0:
            m[i1] = m[i1][::-1]
    return m

for i in snake_matrix(4):
    print(i)

# Snake pattern with comprehension
# lstc = [[i + j if i % 8 < 4 else i + 7 - (j+2) for j in range(1, 5)] for i in range(0, 16, 4)]
# print()
# for i in lstc:
#     print(i)