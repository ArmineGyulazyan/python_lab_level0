def no_repeat(ls):
    x=ls[0]
    for i in ls[1::]:
        x^=i
    return x

print(no_repeat([1,2,2,1,5,4,5]))

