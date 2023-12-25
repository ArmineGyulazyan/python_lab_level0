ls = [1,2,3,4,5,6,10,7,8,9,14]
count = 0
for i in range(len(ls)):
    if ls[i] % 2 != 0:
        count += 1
print(count)