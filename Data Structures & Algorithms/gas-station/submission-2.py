class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(n):
            cur = 0
            for j in range(i, i + n):
                cur = cur + gas[j % n] - cost[j % n]
                if cur < 0: break
                if j == i + n - 1:
                    return i
        
        return -1