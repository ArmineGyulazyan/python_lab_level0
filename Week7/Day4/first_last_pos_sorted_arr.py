def searchRange(self, nums, target):
    st = 0
    end = len(nums) - 1
    first, last = -1, -1
    while st <= end:
        mid = (st + end) // 2
        if nums[mid] == target:
            first = mid
            end = mid - 1
        elif nums[mid] < target:
            st = mid + 1
        elif nums[mid] > target:
            end = mid - 1
    st = 0
    end = len(nums) - 1
    while st <= end:
        mid = (st + end) // 2
        if nums[mid] == target:
            last = mid
            st = mid + 1
        elif nums[mid] < target:
            st = mid + 1
        elif nums[mid] > target:
            end = mid - 1

    return [first, last]