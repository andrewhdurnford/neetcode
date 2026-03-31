class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 1001

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] < nums[l]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
            
            res = min(nums[m], res)
        
        return res