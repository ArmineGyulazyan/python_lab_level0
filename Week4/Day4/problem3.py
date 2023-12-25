def scalar_mul(n,V1,V2):
    mul = [V1[i]*V2[i] for i in range(n)]
    print(mul)
    
    sum_i = 0
    for i in mul:
        sum_i += i
    return sum_i

V1,V2 = [1,2,3,4,5],[5,6,7,3,3]

print(scalar_mul(5,V1,V2))