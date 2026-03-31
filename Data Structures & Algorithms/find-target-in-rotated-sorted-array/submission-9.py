class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        p = 0

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < nums[p]:
                    p = l
                break

            mid = (l + r) // 2
            if nums[mid] < nums[p]:
                p = mid

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        l = 0
        r = len(nums) - 1

        if target >= nums[p] and target <= nums[r]:
            l = p
        else:
            r = p - 1

        
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return -1