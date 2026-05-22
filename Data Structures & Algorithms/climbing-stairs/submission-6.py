class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        dp1, dp2 = 1, 2

        for i in range(3, n + 1):
            dp = dp1 + dp2
            dp1, dp2 = dp2, dp

        return dp

