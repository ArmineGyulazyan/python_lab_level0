ls = [1,24,16,40,8,32,64,128]
for i in range(len(ls)):
	new_el = ls[i]/len(ls)
	ls[i] = new_el

print(ls)