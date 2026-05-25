class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        numSet = set([0])

        for n in nums:
            for i in list(numSet):
                if n + i <= target:
                    numSet.add(n + i)
            
            if target in numSet: return True
        
        return False