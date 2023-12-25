s1 = {1,2,3,5,10,6,7,8}
for i in s1.copy():
    if i % 2 == 1:
        s1.remove(i)
        s1.add(i + 11)
print(s1)

