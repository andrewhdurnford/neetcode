class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        res = 0

        for p in prices:
            if p > buy: 
                res += p - buy
            buy = p
        
        return res
        
