def formula(n,x):
    sum_a = 0
    for i in range(1,n+1):
       sum_a += ((-1)**i)*((x**(i+1))/(fact(3*i)+(2**(i+1))))

    return sum_a

def fact(n):
    return 1 if n in [0,1] else n*fact(n-1)

print(formula(3,4))
print(formula(3,1))
