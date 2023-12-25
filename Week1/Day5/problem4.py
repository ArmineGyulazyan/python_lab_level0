def toHex(num):
    letters = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    str1 = ''
    while num != 0:
        rem = num % 16
        if rem in letters:
           str1 += str(letters[rem])
        else:
            str1 += str(rem)
        num //= 16
    return str1[::-1]


num = int(input("Enter the number: "))
print(toHex(num))