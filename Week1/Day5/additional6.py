def is_polindrome(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return str_num

def check_pol(num):
    step = 0
    if is_polindrome(num):
        return step
    while not is_polindrome(num):
        num = num + int(str(num)[::-1])
        step += 1
    return step


num = int(input("enter the num: "))
print(check_pol(num))
