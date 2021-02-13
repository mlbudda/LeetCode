# %%
# 217. Contains Duplicate
# * Accepted. using hashMap
def containsDuplicate_V2(nums):
    nums_hash = {}
    for i in nums:
        if i in nums_hash:
            return True
        else:
            nums_hash[i] = ''   
    return False

print(containsDuplicate_V2([1,2,3,4]) == False)
print(containsDuplicate_V2([1,2,3,4,1]) == True)

#%%
# 217. Contains Duplicate
# * Brute force method, Time Limit Exceeded
def containsDuplicate_V1(nums):
    for i in nums:
        if nums.count(i)>1:
            return True
    return False


print(containsDuplicate_V1([1,2,3,4]) == False)
print(containsDuplicate_V1([1,2,3,4,1]) == True)
