class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        cur = res = 0
        for n in num_set:
            if n + 1 not in num_set:
                cur = 1
            
                while n - cur in num_set:
                    cur += 1
            
            res = max(cur, res)
        
        return res

            