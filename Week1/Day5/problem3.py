def digitize(num):
    ls = []
    while num != 0:
        digit = num % 10
        ls.append(digit)
        num //= 10
    return ls[::-1]
num = int(input("Enter to digitize: "))
print(digitize(num))