class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        l, res = 0, 0

        for n in nums:
            cnt[n] += 1
            if cnt[n] > l:
                l = cnt[n]
                res = n
        
        return res

        