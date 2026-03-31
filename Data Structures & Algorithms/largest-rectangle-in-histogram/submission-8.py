class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for n, h in enumerate(heights):
            start = n
            
            while stack and h < stack[-1][1]:
                maxArea = max(maxArea, stack[-1][1]*(n - stack[-1][0]))
                start = stack[-1][0]
                stack.pop()

            stack.append([start, h])
        
        while stack:
            maxArea = max(maxArea, stack[-1][1]*(len(heights) - stack[-1][0]))
            stack.pop()
        
        return maxArea
            