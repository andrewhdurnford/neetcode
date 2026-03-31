class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        count = res = 0
        
        for i in range(len(gas) - 1):
            count += gas[i] - cost[i]

            if count < 0:
                count = 0
                res = i + 1
        
        return res