class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set()

        for n in nums:
            numset.add(n)

        for i, n in enumerate(nums):
            cur = 1
            if n - 1 not in numset:
                find = n + 1
                while find in numset:
                    cur += 1
                    find += 1
            res = max(res, cur)
        
        return res