# '''
# 1 2 3
# 4 5 6
# 7 8 9
# '''
# for i in range(0,9,3):
#     for j in range(1,4):
#         print(i+j,end=' ')
#     print()
# # 0+1 0+2 0+3
# # 3+1 3+2 3+3
# # 6+1 6+2 6+3
# print('with Comprehension')
# lst = [[i+j for j in range(1,5)] for i in range(0,16,4)]
# for i in lst:
#     print(i)
# #Snake pattern with comprehension
# lstc = [[i + j if i % 8 < 4 else i + 7 - (j+2) for j in range(1, 5)] for i in range(0, 16, 4)]
# print()
# for i in lstc:
#     print(i)
#spiral form
lst = [[i+j for j in range(1,5)]for i in range(0,16,4)]
for i in lst:
    print(i)
row_st = 0
row_end = len(lst)-1
col_st = 0
col_end = len(lst[0])-1

while row_st<=row_end and col_st<=col_end:
    for i in range(col_st,col_end+1):
        print(lst[row_st][i],end=' ')
    row_st = row_st+1

    for i in range(row_st,row_end+1):
        print(lst[i][col_end],end=' ')
    col_end = col_end-1

    if row_st<=row_end:
        for i in range(col_end,col_st-1,-1):
            print(lst[row_end][i],end=' ')
        row_end = row_end-1

    if col_st<=col_end:
        for i in range(row_end,row_st-1,-1):
            print(lst[i][col_st],end=' ')
        col_end = col_st+1
