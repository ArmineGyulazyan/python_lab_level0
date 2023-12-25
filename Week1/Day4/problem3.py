def fact(num):

    if num in [0,1]:
        return 1
    mul = num
    for i in range(1,num):
        mul = mul * i #4*1=4,4*2=8,8*3=24

    return mul

print(fact(4))
