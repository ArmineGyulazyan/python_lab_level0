def max_myversion(iterable):
    tmp_max = 0
    for i in iterable:
        if tmp_max <= i:
            tmp_max = i
    return tmp_max

print(max_myversion([1,2,3,4,5]))
print(max_myversion([7,2,2,5,6]))
print(max_myversion((0,2,8,5,6)))
print(max_myversion({7:12,2:15,2:8,5:50,30:2}))
#print(max({'a':12,'b':15,'c':8}))  c