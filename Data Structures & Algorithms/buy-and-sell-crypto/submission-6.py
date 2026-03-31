class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        buy = prices[0]

        for p in prices:
            if p < buy:
                buy = p
            
            profit = p - buy
            maxP = max(maxP, profit)
        
        return maxP
            