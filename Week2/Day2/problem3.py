def binary_search_rec(ls,target,start,end):
    if start > end:
        return -1
    if len(ls) != 0:
        mid = (start + end) // 2
        if ls[mid] == target:
            return mid
        if ls[mid] > target:
            #end = mid - 1
            return binary_search_rec(ls,target,start,mid-1)
        if ls[mid] < target:
            #start = mid + 1
            return binary_search_rec(ls,target,mid+1,end)
lst = [1,2,3,4,5,6,7]
print(binary_search_rec(lst,9,0,len(lst)-1))