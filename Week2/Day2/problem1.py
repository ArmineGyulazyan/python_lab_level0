def fib_rec(num):
    if num in [1,2]:
        return num-1
    return fib_rec(num-1)+fib_rec(num-2)

print(fib_rec(1))