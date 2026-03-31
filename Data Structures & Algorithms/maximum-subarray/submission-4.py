class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur, res = 0, nums[0]

        for i in range(len(nums)):
            if cur < 0:
                cur = 0         
            cur += nums[i]
            res = max(res, cur)
            
        return res
            