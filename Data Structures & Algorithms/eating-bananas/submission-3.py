class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        mini = 1000000001

        while l <= r:
            mid = (l + r) // 2
            t = 0
            print('mid:', mid)
            for p in piles:
                t += math.ceil(p / mid)
                print('pile:', math.ceil(p / mid))
            print('total:', t)

            if t > h:
                l = mid + 1
                print('l', l)
            elif t <= h:
                if mid < mini: mini = mid
                r = mid - 1
                print('r', r)

            
        
        return mini