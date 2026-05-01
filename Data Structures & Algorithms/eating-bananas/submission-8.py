class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = max(piles)

        while l <= r:
            m = (l + r) // 2
            print(l, r, m)

            res = 0

            for p in piles:
                res += math.ceil(p / m)
            
            if res <= h:
                result = min(result, m)
                r = m - 1
            else:
                l = m + 1
        
        return result