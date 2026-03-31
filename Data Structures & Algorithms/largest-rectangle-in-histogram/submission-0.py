class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        for i in range(len(heights)):
            if not stack or heights[i] > stack[-1][0]:
                stack.append([heights[i], i])
            else:
                while stack and stack[-1][0] > heights[i]:
                    area = stack[-1][0] * (i - stack[-1][1])
                    if area > largest: largest = area
                    last = stack[-1][1]
                    stack.pop()
                if not stack or stack[-1][0] < heights[i]:
                    stack.append([heights[i], last])
        while stack:
            area = stack[-1][0] * (len(heights) - stack[-1][1])
            if largest < area: largest = area
            stack.pop()
        
        return largest

