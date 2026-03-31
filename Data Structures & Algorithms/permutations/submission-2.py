class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(cur, used):
            nonlocal res
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    cur.append(nums[i])
                    backtrack(cur, used)
                    used[i] = False
                    cur.pop()
            
        backtrack([], [False] * len(nums))
        return res
