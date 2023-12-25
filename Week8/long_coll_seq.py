count = 0
for num in range(13,15):
    chain = num
    cou = 1
    while chain != 1:
        cou+=1
        if chain % 2 == 0:
            chain = chain/2
        else:
            chain = (3*chain)+1
    count = max(count,cou)
    n=num
print(n,count)




