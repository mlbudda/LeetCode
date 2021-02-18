#%%
# 303. Range Sum Query - Immutable
# * Success
# Runtime: 1104 ms, faster than 28.45%
# Memory Usage: 17.4 MB, less than 91.80%
class NumArray:
    def __init__(self, nums):
        self.nums = nums
    
    def sumRange(self, i,j):
        return sum(self.nums[i:j+1])

obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,2)
param_2 = obj.sumRange(2,5)
param_3 = obj.sumRange(0,5)

# Running some tests...
print(param_1 == 1)
print(param_2 == -1)
print(param_3 == -3)
