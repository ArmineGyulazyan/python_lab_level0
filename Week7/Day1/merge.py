def merge(intervals):
    res = []
    intervals.sort()
    res.append(intervals[0])

    for i in range(1, len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
    return res

    # ls=[]
    # row=[]
    # for i in range(len(intervals)):
    #     for j in range(len(intervals[0])-1):
    #         if intervals[i][j] <= intervals[i+1][j] and intervals[i][j] <= intervals[i-1][j+1]:
    #             row.append(intervals[i-1][j])
    #             row.append(intervals[i][j+1])
    #             ls.append(row)
    #         else:
    #             ls.append(intervals[i])
    # return ls
print(merge([[1,3]]))
print(merge([[1,3],
             [2,6],
             [8,10],
             [15,18]]))
print(merge([[1,4],
             [1,5]]))