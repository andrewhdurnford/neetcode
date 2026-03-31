class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def backtrack(cur, i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            backtrack(cur, i + 1)
            n = cur.pop()

            while i < len(nums) and nums[i] == n:
                i += 1

            backtrack(cur, i)
        
        backtrack([], 0)
        
        return res