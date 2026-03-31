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
            cur.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(cur, i + 1)
        
        backtrack([], 0)
        return res
