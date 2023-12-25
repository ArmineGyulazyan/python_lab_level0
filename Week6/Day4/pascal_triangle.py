def pascal_triangle(numRows):
    lst=[i*[1] for i in range(1,numRows+1)]

    for i in range(2, len(lst)):
        for j in range(1,len(lst[i])-1):
            lst[i][j]=lst[i-1][j]+lst[i-1][j-1]
    return lst

print(pascal_triangle(5))
print(pascal_triangle(3))

