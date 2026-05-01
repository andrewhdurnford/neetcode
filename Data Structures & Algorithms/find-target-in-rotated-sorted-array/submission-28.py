class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            if nums[r] < nums[m]:
                if target <= nums[r] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[r] >= nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m -1
        return -1