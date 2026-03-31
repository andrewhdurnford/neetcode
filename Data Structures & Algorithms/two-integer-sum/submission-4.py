class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = defaultdict(int)
        indices = {}
        for i, n in enumerate(nums):
            if found[target - n] != 0:
                return [indices[target - n], i]
            else:
                found[n] = 1
                indices[n] = i

