class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        res = 1
        l = 1
        r = nums[0] + 1

        while r < len(nums):
            res += 1
            nextI = None
            nextDist = 0

            for i in range(l, r):
                if i + nums[i] > nextDist:
                    nextI = i
                    nextDist = i + nums[i]
                
            l = r
            r = nextDist + 1
        
        return res
            
            