def merge(ls):
    if len(ls) > 1:
        mid = len(ls)//2
        left = ls[:mid]
        right = ls[mid:]

        merge(left)
        merge(right)

        i = j = k = 0
        while i < len(left) and j<len(right):
            if left[i] <= right[j]:
                ls[k] = left[i]
                i+=1
            else:
                ls[k] = right[j]
                j+=1
            k+=1

        while i <len(left):
            ls[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            ls[k]=right[j]
            j += 1
            k += 1
    return ls

print(merge([9,7,8,3,2,1]))