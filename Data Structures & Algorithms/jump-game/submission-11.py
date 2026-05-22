class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi = 0

        for i in range(len(nums)):
            if i > maxi:
                return False
            if i + nums[i] >= maxi: 
                maxi = i + nums[i]
            if maxi >= len(nums) - 1:
                return True

        return False