class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        bought = 101
        
        for p in prices:
            if p < bought:
                bought = p
            
            res = max(res, p - bought)

        return res
