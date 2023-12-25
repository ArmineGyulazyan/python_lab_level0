def div(n):
    sum_i = 0
    for i in range(1, n):
        if n % i == 0:
            sum_i += i
    return sum_i

def friend():
    for num in range(1, 10000):
        first = div(num)
        if div(first) == num and first != num:
            yield (num, first)


for i in friend():
    print(i)