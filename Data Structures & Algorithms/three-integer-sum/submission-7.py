class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            if i > 0 and n == nums[i - 1]:
                continue 
            
            while l < r:
                val = n + nums[l] + nums[r]
                if val == 0:
                    res.append([n, nums[l], nums[r]])
                    
                    t = nums[l]
                    while nums[l] == t and l < r:
                        l += 1
                    
                    t = nums[r]
                    while nums[r] == t and l < r:
                        r -= 1

                elif val < 0:
                    l += 1

                elif val > 0:
                    r -= 1
        
        return res