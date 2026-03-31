class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        
        dp = set()
        dp.add(0)

        for n in nums:
            
            nextDP = set()
            
            for p in dp:
                if p + n == target: 
                    return True
                nextDP.add(p + n)
                nextDP.add(p)
            
            dp = nextDP
        
        return False

