#%%
# 53. Maximum Subarray
# * Success
# Runtime: 72 ms, faster than 91.95%
# Memory Usage: 15 MB, less than 82.12%
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

# %%
# 53. Maximum Subarray
# * Success
# Runtime: 72 ms, faster than 29.92%
# Memory Usage: 15 MB, less than 36.62%
def max_sub_array(nums):
    if not nums:
        return 0

    n = len(nums)
    
    res, s, s_pre = nums[0], nums[0], nums[0]

    for i in range(1, n):
        s= max(nums[i], s_pre + nums[i])
        s_pre = s
        res = max(res, s)
    return res

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6)
print(max_sub_array([1]) == 1)
print(max_sub_array([0]) == 0)
print(max_sub_array([-1]) == -1)
print(max_sub_array([-100000]) == -100000)