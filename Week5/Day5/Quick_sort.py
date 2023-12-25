def partition(array,start,end):
    pivot = array[end]

    i = start-1

    for j in range(start,end):
        if array[j]<=pivot:
            i = i + 1
            array[i],array[j] = array[j],array[i]
    i+=1
    array[i],array[end] = array[end],array[i]
    return i

def quick_sort(array,start,end):
    if start < end:
        pi = partition(array,start,end)
        quick_sort(array,start,pi-1)
        quick_sort(array,pi+1,end)
    return array

d=[5,4,7,2]
print(quick_sort(d,0,len(d)-1))