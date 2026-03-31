class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, maxi, profit = 101, 0, 0

        for p in prices:
            mini = min(mini, p)
            profit = p - mini
            if profit > maxi: maxi = profit

        return maxi



