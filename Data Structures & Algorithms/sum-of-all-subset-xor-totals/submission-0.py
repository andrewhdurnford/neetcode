class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [[]]
        res = 0

        for n in nums:
            subsets.extend([s + [n] for s in subsets]) 

        for s in subsets:
            if s:
                cur = 0
                for n in s:
                    cur ^= n
        
                res += cur
        return res