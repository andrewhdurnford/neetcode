class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        cur = 0

        for n in nums:
            cur += n

            if cur - k in prefix:
                res += prefix[cur - k] 
            
            prefix[cur] += 1
        
        return res