class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        if len(nums) == 1: return 1
        res = 1

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
                    res = max(res, LIS[i])
        
        return res