class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2: return min(cost)
        minCost = cost.copy()

        for i in range(2, len(cost)):
            minCost[i] += min(minCost[i - 1], minCost[i - 2])
        
        return min(minCost[-1], minCost[-2])