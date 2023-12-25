ls = [1,45,-7,8,1,12]
max_s = 0
for i in range(0,len(ls)-3):
    res = 0
    for j in range(i,i+3):
        res += ls[j]
    if res >= max_s:
        max_s = res
print(max_s)
