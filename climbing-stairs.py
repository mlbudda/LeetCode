#%%
# 70. Climbing Stairs
# * Success
# Runtime: 28 ms, faster than 82.74%
# Memory Usage: 14.3 MB, less than 13.70%
def climbStairs_V1(n):
    if n < 2: return n
    elif n == 2: return 2
    elif n == 3: return 3
    else:
        result = [2,3]
        for _ in range(n-3):
            result.append(sum(result))
            del result[0]
        return result[1]

# Running some test..
print(climbStairs_V1(0) == 0)
print(climbStairs_V1(1) == 1)
print(climbStairs_V1(2) == 2)
print(climbStairs_V1(3) == 3)
print(climbStairs_V1(4) == 5)
print(climbStairs_V1(5) == 8)
print(climbStairs_V1(6) == 13)
print(climbStairs_V1(7) == 21)
print(climbStairs_V1(8) == 34)
print(climbStairs_V1(9) == 55)

#%%
# 70. Climbing Stairs
# * Success
# Runtime: 32 ms, faster than 56.14%
# Memory Usage: 14.3 MB, less than 47.77%
def climbStairs_V2(n):
    if n < 2 or n == 2: return n
    result = [1,2]
    for _ in range(n-2):
        result.append(sum(result))
        del result[0]
    return result[1]

# Running some test..
print(climbStairs_V2(0) == 0)
print(climbStairs_V2(1) == 1)
print(climbStairs_V2(2) == 2)
print(climbStairs_V2(3) == 3)
print(climbStairs_V2(4) == 5)
print(climbStairs_V2(5) == 8)
print(climbStairs_V2(6) == 13)
print(climbStairs_V2(7) == 21)
print(climbStairs_V2(8) == 34)
print(climbStairs_V2(9) == 55)