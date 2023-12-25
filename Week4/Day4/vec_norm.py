def norm(V1):
    sum_v = 0
    for i in range(len(V1)):
        sum_v += (V1[i] * V1[i])
    return sum_v ** 0.5


V1 = [3, 4]
print(norm(V1))