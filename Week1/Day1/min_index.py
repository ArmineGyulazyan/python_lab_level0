ls = [1,2,2,6,5,7,8,2,3]
tmp = ls[0]
index = 0
for i in range(1,len(ls)):
	if ls[i] <= tmp:
		tmp = ls[i]
		index = i
print(index)