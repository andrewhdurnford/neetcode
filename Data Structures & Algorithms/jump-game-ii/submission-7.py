class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        res = 1 # number of jumps
        l = 0 # where we are
        r = nums[0] # where we can go

        while r < len(nums) - 1: # we havent reached the end
            res += 1
            nxt = None # where we are going
            maxi = 0 # how far that gets us
            for i in range(l + 1, r + 1): # check each index we can visit
                if i + nums[i] > maxi:
                    nxt = i
                    maxi = i + nums[i]
            
            l = nxt
            r = maxi
        
        return res

