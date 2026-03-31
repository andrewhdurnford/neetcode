class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cMin, cMax = 1, 1

        for n in nums:
            tmp = cMax * n
            cMax = max(n * cMax, n * cMin, n)
            cMin = min(tmp, n * cMin, n)
            res = max(res, cMax)
        
        return res


