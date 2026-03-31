class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(h)):
            if not stack:
                stack.append([h[i], i])
            else:
                idx = i
                while stack and h[i] < stack[-1][0]:
                    res = max(res, stack[-1][0] * (i - stack[-1][1]))
                    idx = stack.pop()[1]
                stack.append([h[i], idx])
        
        while stack:
            res = max(res, stack[-1][0] * (len(h) - stack[-1][1]))
            stack.pop()

        return res