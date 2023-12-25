s = 0
for a in range(100):
    for b in range(100):
        poww = a**b
        dig_sum = sum(int(i) for i in str(poww))
        s = max(s,dig_sum)
print(s)