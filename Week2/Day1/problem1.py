def numtoZero(num):
    if num < 0:
        return 0

    print(num)
    numtoZero(num-1)

numtoZero(10)