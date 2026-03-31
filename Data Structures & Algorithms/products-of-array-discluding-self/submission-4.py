class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        before = [0] * n
        after = [0] * n

        before[0] = after[n-1] = 1

        for i in range(1, len(nums), 1):
            before[i] = before[i - 1] * nums[i - 1]
        
        for i in range(len(nums)-1, -1, -1):
            if i == (n - 1): continue
            after[i] = after[i + 1] * nums[i + 1]
        
        
        for i, n in enumerate(nums):
            result[i] = before[i] * after[i]
        
        return result