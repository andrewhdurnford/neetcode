class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        right = len(nums) - 1
        res = []

        for i, n in enumerate(nums):
            if n > 0: 
                break

            if i > 0 and n == nums[i - 1]:
                continue

            l = i + 1
            r = right 

            while l < r:
                summ = n + nums[l] + nums[r]
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    res.append((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

            
        return list(set(res))
            