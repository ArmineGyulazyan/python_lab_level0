def mapp(iterable,func):
    return [func(i) for i in iterable]


def triple(data):
    return data*3

base = [1,2,3,4,5,6,7,8,9,10]
print(mapp(base,triple))
