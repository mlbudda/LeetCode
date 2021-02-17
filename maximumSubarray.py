#%%
# 53. Maximum Subarray
def maxSubArray(nums):
    max_here = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        max_here = max(nums[i], max_here + nums[i])
        result = max(result, max_here)
    return result


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(maxSubArray([1]) == 1)
print(maxSubArray([0]) == 0)
print(maxSubArray([-1]) == -1)
print(maxSubArray([-100000]) == -100000)

