class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = 0
        if target > nums[-1]: return len(nums)

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
                res = m
        
        return res