class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res_set = set()
        nums = sorted(nums)

        def backtrack(sub, i):
            if i == len(nums):
                res_set.add(tuple(sub))
                return

            sub.append(nums[i])
            backtrack(sub, i + 1)
            sub.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(sub, i + 1)
        
        backtrack([], 0)
        res = []
        for r in res_set:
            res.append(list(r))
        
        return res
            
