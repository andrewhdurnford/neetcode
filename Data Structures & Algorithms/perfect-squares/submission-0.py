class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            j = 1
            while j ** 2 <= i:
                if j ** 2 == i:
                    dp[j ** 2] = 1
                else:
                    x = i - j ** 2
                    if dp[i] == 0:
                        dp[i] = dp[x] + 1
                    dp[i] = min(dp[i], dp[x] + 1) 
                j += 1
        
        return dp[-1]
                
