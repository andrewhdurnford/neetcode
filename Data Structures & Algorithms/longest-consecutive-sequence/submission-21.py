class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for i in range(len(nums)):
            
            if nums[i] - 1 in numset:
                continue
            
            cur = 1
            n = nums[i] 

            while n + 1 in numset:
                cur += 1
                n += 1
            res = max(res, cur)

        return res