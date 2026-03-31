class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        before = [1] * len(nums)
        res = [1] * len(nums)
        after = [1] * len(nums)

        # Before
        for i in range(1, l):
            before[i] = before[i - 1] * nums[i - 1]
        
        # After
        for i in range(l - 2, -1, -1):
            after[i] = after[i + 1] * nums[i + 1]
        
        # Res
        for i in range(l):
            res[i] = before[i] * after[i]
        
        return res
