class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h))
                res = max(res, h)
                continue

            idx = i
            while stack and h <= stack[-1][1]:
                idx, prevH = stack.pop()
                res = max(res, prevH * (i - idx))
            
            stack.append((idx, h))

        while stack:
            idx, h = stack.pop()
            res = max(res, h * (len(heights) - idx))
        
        return res

            

