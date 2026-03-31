class Solution:
    def trap(self, h: List[int]) -> int:
        w = 0
        maxL = h[0]
        maxR = h[-1]
        l = 0
        r = len(h) - 1
        while (l < r):
            if maxL < maxR:
                l += 1
                if h[l] < maxL:
                    w += maxL - h[l]
                else:
                    maxL = h[l]
            else:
                r -= 1
                if h[r] < maxR:
                    w += maxR - h[r]
                else:
                    maxR = h[r]
        return w

