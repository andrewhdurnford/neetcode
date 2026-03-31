class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = l + ((r - l) // 2)
            t = 0
            for p in piles:
                t += math.ceil(p / m)
            
            if t > h:
                l = m + 1
            elif t <= h:
                r = m - 1
                res = min(res, m)
        
        return res
            