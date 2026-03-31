class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = defaultdict(int)

        for i, n in enumerate(numbers):
            if nums[target - n] != 0:
                return [nums[target - n], i + 1]
            nums[n] += i + 1

