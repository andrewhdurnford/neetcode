class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize result and stack
        largest = 0
        stack = []

        for i, h in enumerate(heights):
            last = i
            # While shorter than top of stack, calculate area and pop
            while stack and heights[i] < stack[-1][0]:
                height, last = stack.pop()
                area = height * (i - last)
                if largest < area: largest = area

            # Push to stack
            if not stack or heights[i] > stack[-1][0]:
                stack.append([heights[i], last])


        while stack:
            area = stack[-1][0] * (len(heights) - stack[-1][1])
            if largest < area: largest = area
            stack.pop()
        
        return largest

