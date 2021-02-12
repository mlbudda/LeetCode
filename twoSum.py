# %%
# One pass HashMap
def twoSum(nums, target):
    stored_map = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in stored_map:
            return [stored_map[diff], i]
        stored_map[n] = i
    return

# Run some test...
print(twoSum([2,7,11,15], 9) == [0,1])
print(twoSum([3,2,4], 6) == [1,2])
print(twoSum([3,3], 6) == [0,1])

