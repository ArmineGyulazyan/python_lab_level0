num = int(input("Enter the size: "))
ls = []
for i in range(num):
	inp_int = int(input())
	if isinstance(inp_int,int):
		ls.append(inp_int)
print(ls)