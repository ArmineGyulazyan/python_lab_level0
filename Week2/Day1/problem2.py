def zerotoNum(num):
    if num < 0:
        return 0

    zerotoNum(num-1)
    print(num)

zerotoNum(10)