class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = 1001

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res

            m = l + ((r - l) // 2)
            res = min(res, nums[m])

            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return res
            