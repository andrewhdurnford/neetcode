class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, res = 0, max(piles), max(piles)

        while l <= r:
            m = (l + r) // 2
            t = 0
            if m == 0:
                break

            for p in piles:
                t += math.ceil(p / m)

            if t <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res
            
