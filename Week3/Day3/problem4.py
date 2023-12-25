def reverse_slice(lst):
    l1=lst[::-1]
    return l1[1:5:2]


lst = [8, 2, 3, 4, 5, 6, 7]
print(reverse_slice(lst))