matrix = [[i+j for j in range(1,5)] for i in range(0,16,4)]
mat = matrix[:4:3]
for i in matrix:
    print(i)
print()

for i in mat:
    print(i)

for i in mat:
    print(min(i) + max(i))

