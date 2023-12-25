# def remove_duplicates(nums):
#     di = {}
#     for i in range(len(nums)):
#         if nums[i] not in di:
#             di[nums[i]] = i
#
#     return list(di)
#
# print(remove_duplicates([1,1,2,2,3]))

#method2 in-place
'''
def remove_duplicates(nums):
    nums[:] = sorted(set(nums))
    return nums

k = remove_duplicates([5,1,1,2,2,3])
print(k)
'''
def remove_duplicates(nums):
    j=0
    for i in range(1,len(nums)):
        if nums[j] != nums[i]:
            j+=1
            nums[j] = nums[i]
    for el in range(j+1,len(nums)):
        nums[el] = '_'

    return nums,j+1
print(remove_duplicates([1,1,2,2,3]))

