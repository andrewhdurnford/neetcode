class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split(largest):
            sub = 1
            cur = 0

            for n in nums:
                if cur + n <= largest:
                    cur += n
                else:
                    sub += 1
                    if sub > k:
                        return False
                    cur = n
            
            return True
        
        l, r = max(nums), sum(nums)

        res = r

        while l <= r:
            m = l + ((r - l) // 2)

            if split(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res