def filter(iterable,func):
    return [i for i in iterable if func(i)]


def evens(data):
    return True if data%2==0 else False

base = [1,2,3,4,5,6,7,8,9,10]
print(filter(base,evens))
