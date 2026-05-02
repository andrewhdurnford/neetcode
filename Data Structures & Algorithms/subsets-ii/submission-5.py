class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]

        def backtrack(cur, idx):
            if idx == len(nums):
                return
            
            i = idx
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            backtrack(cur, i)

            cur.append(nums[idx])
            res.append(cur.copy())
            backtrack(cur, idx + 1)
            cur.pop()

        backtrack([], 0)
        return res
        