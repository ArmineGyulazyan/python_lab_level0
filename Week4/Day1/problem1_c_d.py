#c
print('----Increasing order----')
def digit_increase(num):
    while num != 0:
        dig = num % 10
        tmp = dig
        num //= 10
        if (num%10) > tmp:
            return 'Not increasing'
    return 'YES'

print(digit_increase(358))

#d
print('----NOT decreasing order----')
def not_digit_decrease(num):
    while num != 0:
        dig = num % 10
        tmp = dig
        num //= 10
        if (num%10) > tmp:
            return 'Decreasing or other'
    return 'YES'

print(not_digit_decrease(358))
print(not_digit_decrease(581))
print(not_digit_decrease(351))
