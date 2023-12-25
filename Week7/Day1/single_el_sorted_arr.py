def singleNonDuplicate(self, nums):
    st = 0
    end = len(nums) - 1
    while st < end:
        mid = (st + end) // 2
        if mid % 2 == 0:
            if nums[mid] ^ nums[mid + 1] == 0:
                st = mid + 2
            else:
                end = mid
        else:
            if nums[mid] ^ nums[mid + 1] == 0:
                end = mid - 1
            else:
                st = mid + 1
    return nums[st]

