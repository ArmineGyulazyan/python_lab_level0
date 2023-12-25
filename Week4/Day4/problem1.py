def mul_vec(k,V):
    for i in range(len(V)):
        V[i] *= k
    return V

n = 5
V = []
for i in range(n):
    V.append(i)
print(mul_vec(2,V))