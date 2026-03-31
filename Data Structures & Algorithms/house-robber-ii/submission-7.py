class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dp(s, e):
            if len(nums) == 1:
                return nums[0]
        
            if len(nums) == 2:
                return max(nums[0], nums[1])
            
            h1 = nums[s]
            h2 = max(nums[s], nums[s + 1])

            for i in range(s + 2, e):
                tmp = h2
                h2 = max(h1 + nums[i], h2)
                h1 = tmp 

            return h2
        
        return max(dp(1, len(nums)), dp(0, len(nums) - 1))
