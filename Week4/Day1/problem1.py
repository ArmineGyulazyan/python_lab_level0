#a
print('----3 Digit----')
def digit3(num):
    while num != 0:
        dig = num % 10
        if dig == 3:
            return 'YES'
        num //= 10
    return 'NO 3'

print(digit3(2511))

#b
print('----5 Digit----')
def digit5(num):
    while num != 0:
        dig = num % 10
        if dig == 5:
            return 'There is 5'
        num //= 10
    return 'Yes'

print(digit5(35113))

#e
print('----Digit Sum----')
def digit_sum(num):
    sum = 0
    while num != 0:
        dig = num % 10
        sum += dig
        num //= 10
    if sum > 20:
        return 'YES'
    return 'Less than 20'

print(digit_sum(3511))

#f
print('----Digit Multiplication----')
def digit_mul(num):
    mul = 1
    while num != 0:
        dig = num % 10
        mul *= dig
        num //= 10
    if mul < 30:
        return 'YES'
    return 'More than 30'

print(digit_mul(718))