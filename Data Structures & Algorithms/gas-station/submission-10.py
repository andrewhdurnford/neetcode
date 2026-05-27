class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if total of gas >= cost, there is a solution 
        if sum(gas) < sum(cost):
            return -1
        
        cur = 0
        res = 0

        for i in range(len(gas)):
            cur += gas[i] - cost[i]

            if cur < 0:
                res = i + 1
                cur = 0
        
        return res