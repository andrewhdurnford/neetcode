class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if m > 0 and nums[m] < nums[m - 1]:
                return nums[m]
                
            if nums[l] > nums[r] and nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return nums[m]