ls = [1,2,2,6,5,10,1,2,3]
max = ls[0]
min = ls[0]
sum = 0
for i in range(1,len(ls)):
	if ls[i] >= max:
		max = ls[i]
	if ls[i] <= min:
		min = ls[i]
sum = max+min
print(sum)