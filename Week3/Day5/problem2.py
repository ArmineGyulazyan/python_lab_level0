def map2(func,data1,data2):

    return [func(data1[i],data2[i]) for i in range(len(data1))]

def exponent(a,b):
    return a**b

# def sum(a,b):
#     return a+b
base = [10,20,30,40,50,60,70,80,90,100]
exp = [1,2,3,4,5,6,7,8,9,10]

print(map2(exponent,base,exp))