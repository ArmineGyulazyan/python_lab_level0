def fact(n):
    if n in [0,1]:
        return 1
    return n*fact(n-1)

# print(fact(100))
# print(fact(10)*3628800)

print(sum(int(i) for i in str(fact(100))))