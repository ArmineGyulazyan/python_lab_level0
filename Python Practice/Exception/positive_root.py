class NegativeNumberError(Exception):
    "The number is negative"
    pass

def positive_root(num):
    if  num < 0:
        raise NegativeNumberError

    return num**0.5

print(positive_root(25))
print(positive_root(-25))