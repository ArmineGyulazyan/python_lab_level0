def evens():
    evens = [i for i in range(1,201) if i % 2 == 0]
    return sum(evens)

print(evens())