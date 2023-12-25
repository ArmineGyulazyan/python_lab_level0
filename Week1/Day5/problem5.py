def bin_num(num):
    binar = ''
    while num != 0:
        rem = num % 2
        binar += str(rem)
        num //= 2
    return binar[::-1]



num = int(input("Enter the number: "))
print(bin_num(num))