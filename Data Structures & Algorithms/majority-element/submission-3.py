import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while True:
            can = random.choice(nums)
            if nums.count(can) > n // 2:
                return can
        