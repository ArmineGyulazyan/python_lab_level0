def fib(n):
    if n in [1,2]:
        return n-1
    sum_f = 0
    prev = 0
    next_i = 1
    for i in range(2,n):
        sum_f = prev + next_i
        prev = next_i
        next_i = sum_f
    return sum_f

print(fib(10))

    #1,1,2,3,5,8,13
    #6->8



