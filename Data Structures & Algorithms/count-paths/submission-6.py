class Solution:
    def uniquePaths(self, m: int, n: int) -> int:    
        if n > m:
            n, m = m, n
        dp1 = [1] * n
        
        for j in range(1, m):      
            dp2 = [1] + [0] * (n - 1)
            for i in range(1, n):
                dp2[i] = dp2[i - 1] + dp1[i]
            dp1 = dp2
        
        return dp1[-1]