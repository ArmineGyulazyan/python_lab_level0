def singleNumber(self, nums):
    # di = {}
    # for i in nums:
    #     if i not in di:
    #         di[i] = 1
    #     else:
    #         di[i]+=1
    # return [i for i in di if di[i]==1]
    res = nums[0]
    for i in nums[1:]:
        res ^= i
    s = set(nums)
    for i in s:
        if res ^ i in s:
            return [i, res ^ i]
