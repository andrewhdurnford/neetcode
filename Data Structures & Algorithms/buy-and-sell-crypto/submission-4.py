class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, maxi, profit = 101, 0, 0
        for i in prices:
            mini = min(mini, i)
            profit = i - mini
            if profit > maxi: maxi = profit
        return maxi