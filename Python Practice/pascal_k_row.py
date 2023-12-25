def getRow( rowIndex):
    lst = [i * [1] for i in range(1, rowIndex + 2)]

    for i in range(2, len(lst)):
        for j in range(1, len(lst[i]) - 1):
            lst[i][j] = lst[i - 1][j] + lst[i - 1][j - 1]
    return lst[rowIndex]

# def getRow(rowIndex):
#     res = [[1]]
#
#     for i in range(rowIndex):
#         temp = [0] + res[-1] + [0]
#         row = []
#
#         for j in range(len(res[-1]) + 1):
#             row.append(temp[j] + temp[j + 1])
#         res.append(row)
#
#     return res[-1]
print(getRow(3))