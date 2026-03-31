class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        l, r  = 0, len(nums) - 1

        while r - l + 1 > k:
            if (abs(nums[l] - x) - abs(nums[r] - x)) <= 0:
                r -= 1
            else:
                l += 1
        
        return nums[l : r + 1]