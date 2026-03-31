class Solution:
    def trap(self, h: List[int]) -> int:
        maxL, maxR = 0, 0
        res = 0
        
        l, r = 0, len(h) - 1

        while l < r:
            maxh = min(maxL, maxR)
            if h[l] < maxh:
                res += maxh - h[l]
            
            if h[r] < maxh:
                res += maxh - h[r]

            maxL = max(h[l], maxL)
            maxR = max(h[r], maxR)

            if h[l] <= h[r]:
                l += 1
            else:
                r -= 1

        return res