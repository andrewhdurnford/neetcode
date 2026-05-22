class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            cur = 0
            for j in range(i, i + n):
                cur += gas[j % n] - cost[j % n]
                j += 1
                if cur < 0: break

            if j - n == i and cur >= 0:
                return i

        return -1
