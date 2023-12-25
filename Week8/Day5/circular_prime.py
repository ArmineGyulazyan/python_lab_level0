def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

num_count = 0
for i in range(2,1000000):
    num = str(i)
    if is_prime(i):
        for j in range(len(num)):
            if not is_prime(int(num[j:] + num[:j])):
                break
        else:
            num_count += 1
print(num_count)
num='17'
print('0 ends ',num[:1])