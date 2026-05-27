class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1

        for n in nums:
            tmp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * tmp, n * curMin, n)
            res = max(res, curMax)
        
        return res