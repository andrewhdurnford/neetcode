class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(cur, i):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            
            if sum(cur) > target:
                return
            
            if i < len(nums) - 1:
                backtrack(cur, i + 1)
            
            if i < len(nums):
                cur.append(nums[i])
                backtrack(cur, i)
                cur.pop()

            return
        
        backtrack([], 0)
        return res