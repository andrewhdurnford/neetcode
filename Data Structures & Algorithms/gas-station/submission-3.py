class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n):
            cur = 0
            for i in range(start, start + n):
                cur += gas[i % n] - cost[(i) % n]
                if cur < 0: break
            
            if cur >= 0: return start
    
        return -1
