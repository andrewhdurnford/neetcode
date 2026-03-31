class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = sorted(nums)
        li = {}
        for n in nums:
            if n - 1 in li.keys():
                li[n] = li[n-1] + 1
            else:
                li[n] = 1
        return max(li.values())