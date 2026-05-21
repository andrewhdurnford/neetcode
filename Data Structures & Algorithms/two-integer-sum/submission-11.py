class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i, n in enumerate(nums):
            if target - n in idx:
                return [idx[target - n], i]
            idx[n] = i