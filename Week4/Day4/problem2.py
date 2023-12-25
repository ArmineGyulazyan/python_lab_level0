def sum_vec(n,V1,V2):

    return [V1[i]+V2[i] for i in range(n)]


V1,V2 = [1,2,3,4,5],[5,6,7,3,3]

print(sum_vec(5,V1,V2))
