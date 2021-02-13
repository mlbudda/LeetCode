#%%
# Success
# Runtime: 60 ms, faster than 86.09%
# Memory Usage: 14.5 MB, less than 86.01%
def twoSum(numbers,target):
    stored_map = {}
    
    for e,i in enumerate(numbers):
        diff = target - i
        if diff in stored_map:
            return [stored_map[diff]+1,e+1]
        stored_map[i] = e

print(twoSum([0,0,3,4],0) == [1,2])
print(twoSum([2,7,11,15],9) == [1,2])
print(twoSum([2,3,4],6) == [1,3])
print(twoSum([-1,0],-1) == [1,2])