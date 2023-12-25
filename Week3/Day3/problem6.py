matrix = [[i+j for j in range(1,6)] for i in range(0,25,5)]
#matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
for i in matrix:
    print(i)
print()
# for i in matrix[0::3]:
#     print('minimum is',min(i))
#     print('maximum is',max(i))
print([i[:3:2] for i in matrix])