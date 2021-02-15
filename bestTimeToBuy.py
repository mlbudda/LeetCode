#%%
# 121. Best Time to Buy and Sell Stock
# * Success
# Runtime: 964 ms, faster than 52.46%
# Memory Usage: 25 MB, less than 59.66%
def maxProfit(prices):
    profit = 0
    if len(prices) > 0: lowest_number = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < lowest_number:
            lowest_number = prices[i]
        elif prices[i] - lowest_number > profit:
            profit = prices[i] - lowest_number
    return profit

print(maxProfit([7,1,5,3,6,4]) == 5)
print(maxProfit([7,6,4,3,1]) == 0)
print(maxProfit([1]) == 0)
print(maxProfit([]) == 0)

#%%
# 121. Best Time to Buy and Sell Stock
# ! Time Limit Exceeded
# 198 / 210 test cases passed.
def maxProfit(prices):
    positive_trades = []
    for e,i in enumerate(prices):
        for j in range(e+1, len(prices)):
            if i < prices[j]:
                positive_trades.append(prices[j] - i)
    if positive_trades:
        return max(positive_trades)
    else:
        return 0

print(maxProfit([7,1,5,3,6,4]) == 5)
print(maxProfit([7,6,4,3,1]) == 0)
print(maxProfit([1]) == 0)
print(maxProfit([]) == 0)

