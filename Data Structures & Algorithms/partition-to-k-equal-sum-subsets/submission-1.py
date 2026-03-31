class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        nums.sort(reverse=True)
        if sum(nums) % k != 0: return False
        target = sum(nums) / k
        parts = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True
            
            for p in range(k):
                if parts[p] + nums[i] <= target:
                    parts[p] += nums[i]
                    if backtrack(i + 1):
                        return True
                    parts[p] -= nums[i]
                
                if parts[p] == 0:
                    return False
                
            return False
        
        return backtrack(0)
