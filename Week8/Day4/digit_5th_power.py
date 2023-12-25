s = set()
for a in range(2,101):
    for b in range(2,101):
        res = a**b
        s.add(res)
print(len(s))
