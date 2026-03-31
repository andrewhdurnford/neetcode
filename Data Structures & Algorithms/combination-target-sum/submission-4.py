class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, cur_sum):
            nonlocal res
            if cur_sum == target:
                res.append(cur.copy())
                return
            
            if i == len(nums) or cur_sum > target:
                return
            
            backtrack(i + 1, cur, cur_sum)

            cur.append(nums[i])
            backtrack(i, cur, cur_sum + nums[i])
            cur.pop()
        
        backtrack(0, [], 0)
        return res
