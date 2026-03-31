class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []

        def dfs(cur, total, i):
            if total == target:
                res.append(cur.copy())
                return

            if total > target or i == len(nums):
                return
            
            cur.append(nums[i])
            dfs(cur, total + nums[i], i + 1)
            cur.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(cur, total, i + 1)
        
        dfs([], 0, 0)
        
        return res