class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dp(nums):
            if len(nums) == 1:
                return nums[0]
        
            if len(nums) == 2:
                return max(nums[0], nums[1])
            
            h1 = nums[0]
            h2 = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                tmp = h2
                h2 = max(h1 + nums[i], h2)
                h1 = tmp 

            return h2
        
        return max(dp(nums[1:]), dp(nums[:-1]))
