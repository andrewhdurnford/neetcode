class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)

        def dp(nums):
            if len(nums) <= 2: return max(nums)

            dp1 = nums[0]
            dp2 = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp = max(dp1 + nums[i], dp2)
                dp1, dp2 = dp2, dp
            
            return dp
        
        return max(dp(nums[1:]), dp(nums[:-1]))