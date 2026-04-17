class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, cur, summ):
            nonlocal res
            if summ == target:
                res.append(cur.copy())
                return
            
            if summ > target or idx >= len(nums):
                return
            
            backtrack(idx + 1, cur, summ)

            cur.append(nums[idx])
            summ += nums[idx]
            backtrack(idx, cur, summ)
            cur.pop()
            summ -= nums[idx]

        backtrack(0, [], 0)
        return res


