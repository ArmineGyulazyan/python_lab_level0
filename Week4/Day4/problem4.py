import problem3
import vec_norm

def cos_angle(n,V1,V2):
    sc_mul = problem3.scalar_mul(n,V1,V2)
    V1_n = vec_norm.norm(V1)
    V2_n = vec_norm.norm(V2)
    return sc_mul/(V1_n*V2_n)

V1, V2 = [1, 2, 3, 4, 5], [5, 6, 7, 3, 3]
print(cos_angle(5, V1, V2))