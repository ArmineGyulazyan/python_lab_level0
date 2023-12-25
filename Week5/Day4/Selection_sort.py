def selection(ls):
    # ascending order
    for i in range(len(ls)):
        min_i = i
        for j in range(i,len(ls)):
            if ls[j]<ls[min_i]:
                min_i = j
        ls[min_i], ls[i] = ls[i], ls[min_i]

    return ls
    #descending order
    # for i in range(len(ls)):
    #     max_i = i
    #     for j in range(i,len(ls)):
    #         if ls[j]>ls[max_i]:
    #             max_i = j
    #     ls[max_i], ls[i] = ls[i], ls[max_i]
    #
    # return ls

print(selection([7,5,4,2]))
print(selection([7,8,4,2,15,33,3]))

