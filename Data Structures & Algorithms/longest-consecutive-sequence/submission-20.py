class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for n in nums:
            i = n
            cur = 1
            while i - 1 in numSet:
                i -= 1
                cur += 1
            res = max(cur, res)

        return res