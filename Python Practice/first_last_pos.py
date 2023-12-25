def first_el(nums,target):
    st = 0
    end = len(nums) - 1
    first,last = -1,-1
    while st <= end:
        mid = (st + end) // 2
        if nums[mid] == target:
            first = mid
            end = mid-1
        elif nums[mid] < target:
            st = mid + 1
        elif nums[mid] > target:
            end = mid - 1

    return first

def last_el(nums, target):
    st = 0
    end = len(nums) - 1
    first, last = -1, -1
    while st <= end:
        mid = (st + end) // 2
        if nums[mid] == target:
            last = mid
            st = mid + 1
        elif nums[mid] < target:
            st = mid + 1
        elif nums[mid] > target:
            end = mid - 1

    return last

def searchRange(nums,target):
    a=first_el(nums,target)
    b=last_el(nums,target)
    return [a,b]

print(searchRange([5,7,7,8,8,10],8))