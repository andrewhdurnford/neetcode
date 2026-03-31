class Solution:
    def trap(self, h: List[int]) -> int:
        maxL, maxR, res = 0, 0, 0
        l, r = 0, len(h) - 1

        while l <= r:
            if h[l] <= h[r]:
                res += max(min(maxL, maxR) - h[l], 0)
                maxL = max(maxL, h[l])
                maxR = max(maxR, h[r])
                l += 1
            else:
                res += max(min(maxL, maxR) - h[r], 0)
                maxL = max(maxL, h[l])
                maxR = max(maxR, h[r])
                r -= 1

            
            

        return res
