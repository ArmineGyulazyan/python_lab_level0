def sel_sort(ls,k):
    for i in range(len(ls)):
        max_i = i
        for j in range(i,len(ls)):
            if ls[max_i]<ls[j]:
                max_i=j
        ls[max_i],ls[i]=ls[i],ls[max_i]
    return ls[k-1]

print(sel_sort([1,5,8,3],2))
#8,5,3,1