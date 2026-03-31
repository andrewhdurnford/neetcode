class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxi, area = 0, 0
        while(i < j):
            area = min(heights[i], heights[j]) * (j-i)
            if area > maxi: maxi = area
            if heights[i] < heights[j]: i += 1
            else: j -= 1
        return maxi
