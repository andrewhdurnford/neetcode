class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, cur):
            if idx == len(nums):
                res.append(cur.copy())
                return
            
            backtrack(idx + 1, cur)

            cur.append(nums[idx])
            backtrack(idx + 1, cur)
            cur.pop()

        backtrack(0, [])
        return res