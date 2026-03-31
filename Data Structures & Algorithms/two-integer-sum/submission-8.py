class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = defaultdict(int)
        for i, n in enumerate(nums):
            if (target - n) in found:
                return [found[target - n], i] 
            else:
                found[n] = i