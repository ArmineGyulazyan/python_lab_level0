s1 = {'a','b','c','d'}
s2 = set('aqwdcb') # 'd', 'c' 'a' 'w' 'b' 'q'
#hatum
print(s1&s2)
print(s1.intersection(s2))
#miavorum
print(s1 | s2)
print(s1.union(s2))
#symmetric difference
print('symm dif',s1.symmetric_difference(s2))
print('symm dif',s2.symmetric_difference(s1))
print('symm dif',(s1|s2)-(s1&s2))
print('symm dif',s1^s2)
#difference
print(s1-s2)
print(s2-s1)
