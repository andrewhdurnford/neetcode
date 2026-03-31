class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        temp = 0
        

        for n, h in enumerate(heights):
            temp = n

            if not stack:
                stack.append([n, h])
                maxArea = max(maxArea, h)
                continue
            
            if h < stack[-1][1]:
                while stack and h < stack[-1][1]:
                    temp = stack[-1][0]
                    maxArea = max(maxArea, (n - stack[-1][0])*stack[-1][1])
                    stack.pop()

            stack.append([temp, h])
        
        while stack:
            maxArea = max(maxArea, stack[-1][1]*(len(heights) - stack[-1][0]))
            stack.pop()

        return maxArea