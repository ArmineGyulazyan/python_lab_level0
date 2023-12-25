def sumOfUnique(self, nums):
    di = {}
    for i in range(len(nums)):
        if nums[i] in di:
            di[nums[i]] += 1
        else:
            di[nums[i]] = 1
    return sum(i for i in di if di[i] == 1)
