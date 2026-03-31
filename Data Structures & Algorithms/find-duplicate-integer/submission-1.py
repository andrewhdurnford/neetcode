class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if i in nums:
                nums.remove(i)
        
        return nums[0]
