class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(cur, i):
            if i == len(nums):
                res.append(cur.copy())
                return
            
            # use the current number
            cur.append(nums[i])
            backtrack(cur, i + 1)
            cur.pop()

            # skip the current number
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            backtrack(cur, i)
        
        backtrack([], 0)
        return res
