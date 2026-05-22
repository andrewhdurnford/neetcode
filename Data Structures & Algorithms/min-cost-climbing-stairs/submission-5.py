class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2: return min(cost)
        dp = [0] * (len(cost) + 1)


        for i in range(3, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 2], dp[i - 2] + cost[i - 3])
            
        print(dp)
        return min(dp[-1] + cost[-1], dp[-2] + cost[-2])
