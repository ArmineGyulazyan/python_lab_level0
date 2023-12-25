def insertion(ls):
    for i in range(1,len(ls)):
        key = ls[i]
        j=i-1
        while j>=0 and ls[j]>key:
            ls[j+1]=ls[j]
            j-=1
        ls[j+1] = key
        print(ls)
    return ls

print(insertion([5,4,9,2,6,3]))