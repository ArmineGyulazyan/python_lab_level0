def two_sum(ls,target):
    di={}
    for ind in range(len(ls)):
        if target-ls[ind] in di:
            return di[target-ls[ind]],ind

        di[ls[ind]] = ind

print(two_sum([1,2,3,7],8))

