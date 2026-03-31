class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)
        ans = r

        while l <= r:
            m = l + ((r - l) // 2)
            cur = 0
            d = 1

            for w in weights:
                if cur + w > m:
                    cur = w
                    d += 1
                else:
                    cur += w

            if d <= days:
                ans = m
                r = m - 1
                
            else:
                l = m + 1

        return ans
        