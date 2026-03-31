class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums):
            
            h1, h2 = 0, 0

            for i in range(len(nums)):
                tmp = h2
                h2 = max(h1 + nums[i], h2)
                h1 = tmp 

            return h2
        
        return max(nums[0], dp(nums[1:]), dp(nums[:-1]))
