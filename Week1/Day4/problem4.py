def num_sum(num):
    sum = 0
    while num != 0:
        dig = num % 10
        sum += dig
        num //= 10
    return sum

num = int(input("Enter a number: "))
print(num_sum(num))