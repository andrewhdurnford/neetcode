class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            
            mid = (l + r) // 2
            time = 0

            for b in piles:
                time += math.ceil(float(b) / mid)

            if time > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res