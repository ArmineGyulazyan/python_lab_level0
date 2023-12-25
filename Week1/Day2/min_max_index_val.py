ls = []
len_ls = 7
max_i = 0
min_i = 0
for i in range(7):
    el = int(input("Enter element: "))
    ls.append(el)
max=ls[0]
min = ls[0]
for i in range(len(ls)):
    if max <= ls[i]:
        max = ls[i]
        max_i = i
    if min >= ls[i]:
        min = ls[i]
        min_i = i
print(ls)
print("max is ",max,"\nmin is",min)
print("max index is ",max_i,"\nmin index is",min_i)
print("diff is ", max_i-min_i)