class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        nums.sort()
        res = []
        print(nums)
        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                l, r = b + 1, len(nums) - 1

                while l < r:
                    cur = nums[a] + nums[b] + nums[l] + nums[r]

                    if cur < target:
                        l += 1
                    elif cur > target:
                        r -= 1
                    else:
                        res.append([nums[a], nums[b], nums[l], nums[r]])
                        l, r = l + 1, r - 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

        return res
                
            



        

        