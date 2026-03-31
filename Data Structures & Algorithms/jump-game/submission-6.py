class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, i + nums[i] + 1):
                if j < len(nums) and dp[j]: 
                    dp[i] = True
            
        return dp[0]