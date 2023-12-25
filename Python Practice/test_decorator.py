def log_function_info(func):
    def wrapper(*args,**kwargs):
        for i in args:
            print(i)
        for i in kwargs:
            print(kwargs[i])

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return func(*args,**kwargs)
    return wrapper

@log_function_info
def add(a,b):
    '''This function adds two numbers.'''
    return a + b

res1 = add(3,4)
#res2 = add(b=1,a=5)
print(add.__name__)
help(add)

# def foo(n=None):
#     if not n:
#         return None
#     yield [1,2,3]
#
# print(bool([]))
# it = foo([])
# print(it)
# print(next(it))