class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            # break if num > 0 since all nums to right > 0 too
            if a > 0:
                break
            # skip if same as last
            if i > 0 and a == nums[i - 1]:
                continue

            # set left right and target
            l = i + 1
            r = len(nums) - 1
            target = -a

            # two pointer loop
            while l < r:
                summ = nums[l] + nums[r]
                if summ == target:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif summ < target:
                    l += 1
                else:
                    r -= 1
        return res
