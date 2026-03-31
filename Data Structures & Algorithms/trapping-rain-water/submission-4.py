class Solution:
    def trap(self, h: List[int]) -> int:
        maxL, maxR = 0, 0
        l, r = 0, len(h) - 1
        res = 0

        while l < r:
            lim = min(maxL, maxR)
            if h[l] < lim:
                res += lim - h[l]

            if h[r] < lim:
                res += lim - h[r]

            maxL = max(maxL, h[l])
            maxR = max(maxR, h[r])

            if h[l] <= h[r]:
                l += 1
            else:
                r -= 1
        
        return res
