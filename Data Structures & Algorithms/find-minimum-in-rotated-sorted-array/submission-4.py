class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]: return nums[l]
        
        while(l <= r):
            mid = (l + r) // 2

            if nums[mid] < nums[l]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            elif nums[l] < nums[mid]:
                return nums[l]
            elif nums[r] < nums[mid]:
                return nums[r]
            else:
                return nums[mid]
            

        return nums[mid]