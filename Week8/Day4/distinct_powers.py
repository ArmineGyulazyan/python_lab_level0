ls=[]
for num in range(1000,(9**5)*5): #9**5*5 kara limit lini
    dig_s = sum([int(i)**5 for i in str(num)])
    if dig_s == num:
        ls.append(num)
print(sum(ls))
