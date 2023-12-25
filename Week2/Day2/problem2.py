def fact_rec(num):
    # if num in [0,1]:
    #     return 1
    # return num*fact_rec(num-1)
    return 1 if num in [0,1] else num*fact_rec(num-1)

print(fact_rec(5))