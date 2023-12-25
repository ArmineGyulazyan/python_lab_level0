def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def cycle(num):
    if is_prime(num):
        st_num = str(num)
        for j in range(len(st_num)):
            if not is_prime(int(st_num[j:] + st_num[:j])):
                return False
        else:
            return True
    return False
print(cycle(519))