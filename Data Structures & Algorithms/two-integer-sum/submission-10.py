class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = defaultdict(int)

        for i, n in enumerate(nums):
            find = target - n
            if find in nums_map:
                return [nums_map[find], i]
            nums_map[n] = i
        
        