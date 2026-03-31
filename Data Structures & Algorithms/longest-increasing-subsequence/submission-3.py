class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1

        for i in range(len(nums)):
            cur = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    cur = max(cur, dp[j])
            dp[i] = cur + 1
            res = max(cur, res)
        return res