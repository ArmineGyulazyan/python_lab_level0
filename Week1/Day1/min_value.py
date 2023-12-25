ls = [1.6,2,2.5,6,5,7,1.2,2,3]
tmp = ls[0]
for i in range(1,len(ls)):
	if ls[i] <= tmp:
		tmp = ls[i]
print(tmp)