def binary_search(lst,target):
    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (start + end) // 2  # 3
        if lst[mid] == target:
            return mid
        if target <= lst[mid]:
            end = mid - 1  # 4
        if target > lst[mid]:
            start = mid + 1
    return -1


lst = [2,3,5,6,7,8,9,10]
target = 11
print(binary_search(lst,target))