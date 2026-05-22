class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        maxi = 0

        for i in range(len(nums) - 1):
            if i + nums[i] > maxi:
                maxi = i + nums[i]
            
            if i == cur:
                cur = maxi
                res += 1
        
        return res