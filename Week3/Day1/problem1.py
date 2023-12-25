def compr(lst):
    return [sum(lst[i]) for i in range(len(lst))]


lst = [[i+j for j in range(1,4)] for i in range(0,8,3)]
for i in lst:
    print(i)
print('\n',compr(lst))

# lst = [sum([i+j for j in range(1,4)]) for i in range(0,8,3)]
# for i in lst:
#     print(i)

