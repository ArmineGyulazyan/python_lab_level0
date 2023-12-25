count = 0
for n in range(1,10):
    for exp in range(22):
        poww = n**exp
        if len(str(poww)) == exp:
            count += 1
print(count)