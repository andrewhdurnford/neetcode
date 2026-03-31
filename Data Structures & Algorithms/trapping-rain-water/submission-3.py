class Solution:
    def trap(self, h: List[int]) -> int:
        trapped = 0
        maxL = h[0]
        maxR=h[-1]
        l = 0
        r = len(h) - 1

        while l < r:
            if maxL < maxR:
                l += 1
                if h[l] < maxL:
                    trapped += maxL - h[l]
                else:
                    maxL = h[l]
            else:
                r -= 1
                if h[r] < maxR:
                    trapped += maxR - h[r]
                else:
                    maxR = h[r]
            

        return trapped
        
