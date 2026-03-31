class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = 1001

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res
            
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res
