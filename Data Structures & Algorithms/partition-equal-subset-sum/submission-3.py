class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        numSet = set([0])

        for n in nums:
            for i in list(numSet):
                numSet.add(n + i)
            
            if total // 2 in numSet: return True
        
        return False