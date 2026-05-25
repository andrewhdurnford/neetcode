class Solution:
    def uniquePaths(self, m: int, n: int) -> int:    
        dp2 = [1] * n
        new = [1] + [0] * (n - 1)
        
        for j in range(1, m):
            dp1 = dp2.copy()
            dp2 = new.copy()
            for i in range(1, n):
                dp2[i] = dp2[i - 1] + dp1[i]
            
        
        return dp2[-1]