def map3(func,data1,data2,data3):

    return [func(data1[i],data2[i],data3[i]) for i in range(len(data1))]

def sum(a,b,c):
    return a+b+c

print(map3(sum,[1,2,3],[10,20,30],[100,200,300]))