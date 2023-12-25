def is_triangle(a,b,c):
    sum = a+b
    dif = abs(a-b)
    if c < sum and c > dif:
        return True
    return False

print(is_triangle(2,6,7))
print(is_triangle(2,6,10))