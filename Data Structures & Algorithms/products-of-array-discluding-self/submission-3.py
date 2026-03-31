class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        before = [0] * n
        after = [0] * n

        before[0] = after[n-1] = 1
        for i in range(1, n):
            before[i] = before[i - 1] * nums[i - 1]
        
        for i in range(n-2, -1, -1):
            after[i] = after[i + 1] * nums[i + 1]
        
        for i in range(0, n):
            result[i] = before[i] * after[i]
            
        return result
