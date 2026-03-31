class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cur = 0
        prefix = { 0 : 1 }

        for n in nums:
            cur += n
            diff = cur - k

            if diff in prefix:
                res += prefix[diff]
            
            prefix[cur] = 1 + prefix.get(cur, 0)

        return res
