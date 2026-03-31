class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target == nums[m]:
                return True

            if nums[l] < nums[m]:
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1

            elif nums[l] > nums[m]:
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                l += 1

        return False