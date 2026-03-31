class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        def dp(nums):
            dp1 = nums[0]
            dp2 = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp3 = max(dp1 + nums[i], dp2)
                dp1 = dp2
                dp2 = dp3
            
            return max(dp1, dp2)
        
        return max(dp(nums[1:]), dp(nums[:-1]))