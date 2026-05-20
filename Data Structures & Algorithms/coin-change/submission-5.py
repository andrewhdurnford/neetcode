class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            for c in coins:
                if i - c == 0:
                    dp[i] = 1

                if i - c > 0 and dp[i - c] > 0:
                    if dp[i] > 0:
                        dp[i] = min(dp[i], dp[i - c] + 1) 
                    else: 
                        dp[i] = dp[i - c] + 1
        
        return dp[-1] if dp[-1] > 0 else -1

