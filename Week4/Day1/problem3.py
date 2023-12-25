def exp_two(number):
    # while n != 1:
    #     if n % 2 != 0:
    #         return False
    #     n /= 2
    # return True
    return number > 0 and (number & (number - 1)) == 0



print(exp_two(32))
print(exp_two(6))
print(exp_two(64))
print(exp_two(36))