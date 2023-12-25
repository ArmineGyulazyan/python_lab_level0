def sum_digit(num):
    if num < 10:
        return num

    return num % 10 + sum_digit(num//10)

print(sum_digit(1555))