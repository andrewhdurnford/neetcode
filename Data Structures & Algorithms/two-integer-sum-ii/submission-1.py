class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        summ = nums[i] + nums[j]
        while (summ != target):
            if summ < target:
                j += 1
                i += 1
            else:
                i -= 1
            summ = nums[i] + nums[j]
        return [i+1, j+1]