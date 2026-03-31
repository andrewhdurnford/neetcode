class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for buy in [0, 1]:
                if buy:
                    buying = dp[i + 1][0] - prices[i] if i < n - 1 else -prices[i]
                    cooldown = dp[i + 1][1] if i < n - 1 else 0
                    dp[i][1] = max(buying, cooldown)
                
                else:
                    selling = dp[i + 2][1] + prices[i] if i < n - 2 else prices[i]
                    cooldown = dp[i + 1][0] if i < n - 1 else 0
                    dp[i][0] = max(selling, cooldown)
        
        return dp[0][1]