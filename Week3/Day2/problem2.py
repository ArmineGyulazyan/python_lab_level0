ls1 = [1,2,3,4,5,6,7]
ls2 = [1,2,3,4,5,6]
s1, s2 = set(ls1), set(ls2)
print(s1-s2) if len(s1) > len(s2) else print(s2-s1)