class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(cur, total, i):
            if total > target or i == len(nums):
                return
            
            if total == target:
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(cur, total + nums[i], i)
            cur.pop()
            dfs(cur, total, i + 1)

        dfs([], 0, 0)
        return res