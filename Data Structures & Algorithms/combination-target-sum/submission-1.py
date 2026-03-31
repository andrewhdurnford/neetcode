class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur, total, i):
            if target == total:
                res.append(cur.copy())
                return

            if i == len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(cur, total + nums[i], i)
            cur.pop()
            dfs(cur, total, i + 1)
        
        dfs([], 0, 0)
        
        return res
            
