def bubble_sort(ls):
    # Best Case
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(ls) - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
                swapped = True
        print(ls)
    return ls

    '''
    '''
    # Worst case O(n^2)
    for i in range(len(ls)):
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]

    return ls


print(bubble_sort([5, 7, 2, 4, 1, 8]))
# print(bubble_sort([1,2,3,4,5]))
# print(bubble_sort([15,15,2,15,1,8]))
# print(bubble_sort([8,7,6,5,4,3]))
