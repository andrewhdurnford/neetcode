class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        lg = 0

        for n in numSet:
            if n - 1 not in numSet:
                length = 1
                while (n + length) in numSet:
                    length = length + 1
                lg = max(length, lg)
        return lg