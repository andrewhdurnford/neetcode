class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        last = len(nums) - 1
        summ = nums[first] + nums[last] 
        while(summ != target):
            if summ < target:
                first = first + 1
            else:
                last = last - 1
            summ = nums[first] + nums[last] 
        return [first+1, last+1]