class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            candidate = n
            cnt = 1
            for j in range(i, len(nums)):
                if nums[j] == candidate: cnt += 1
            
            if cnt >= len(nums) / 2:
                return candidate

        