def find_unique_element(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if mid % 2 == 0:
            if arr[mid] ^ arr[mid + 1] == 0:
                start = mid + 2
            else:
                end = mid
        else:
            if arr[mid] ^ arr[mid - 1] == 0:
                start = mid + 1
            else:
                end = mid - 1

    return start

print(find_unique_element([1,1,2,3,3,4,4]))