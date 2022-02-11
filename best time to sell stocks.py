#brute force
from asyncio.windows_events import INFINITE


def sell(nums):
    profit = 0
    maxprofit = 0
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            profit = max(nums[j] - nums[i],profit)
        maxprofit = max(maxprofit,profit)

    return maxprofit

#o(n) solution 1
def sell1(nums):
    profit = INFINITE
    maxprofit = 0
    for price in nums:
        minprice = min(price,minprice)
        profit = price - minprice
        maxprofit = max(profit,maxprofit)
    return maxprofit                