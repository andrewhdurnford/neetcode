class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while (l <= r):
            m = (l + r) // 2
            if (target < nums[l] and nums[l] <= nums[m] 
            or target < nums[r] and target > nums[m]):
                l = m + 1
            elif (target > nums[r] and nums[r] >= nums[m] 
            or target > nums[l] and target < nums[m]):
                r = m - 1
            else:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    l = m + 1
                else:
                    return m
              
        return -1


             
