class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []

        def dfs(cur, total, i):
            if total == target:
                res.append(cur.copy())
                return
            
            if i == len(nums):
                return
            
            cur.append(nums[i])
            dfs(cur, total + nums[i], i + 1)
            n = cur.pop()

            while i < len(nums) and nums[i] == n:
                i += 1
            dfs(cur, total, i)
        
        dfs([], 0, 0)
        return res
