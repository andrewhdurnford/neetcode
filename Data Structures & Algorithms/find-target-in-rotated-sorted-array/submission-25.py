class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (( r - l) // 2)

            if target == nums[m]:
                return m
            
            # l <= m and m > target
            if nums[l] <= nums[m]:
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            

            else:
                if nums[m] > target or nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1
        
        return - 1