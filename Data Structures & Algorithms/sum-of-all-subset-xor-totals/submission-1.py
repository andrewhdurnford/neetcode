class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0 

        def backtrack(i, sub):
            nonlocal res
            
            xor = 0
            for n in sub:
                xor ^= n
            res += xor
            
            for j in range(i, len(nums)):
                sub.append(nums[j])
                backtrack(j + 1, sub)
                sub.pop()
        
        backtrack(0, [])
        return res