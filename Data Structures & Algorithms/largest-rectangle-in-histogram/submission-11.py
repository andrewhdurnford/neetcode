class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        # iterate over heights
        # if not stack, add height, idx to stack
        # while height < top of stack
        # pop top of stack, cache index
        # check rectangle from cached to i - 1
        # once not stack or height > top of stack
        # append height, cached idx to top of stack

        for i, h in enumerate(heights):
            if not stack:
                stack.append((h, i))
                continue
            
            idx = i
            while stack and h < stack[-1][0]:
                prev, idx = stack.pop()
                res = max(res, prev * (i - idx))
            
            stack.append((h, idx))

        while stack:
            prev, idx = stack.pop()
            res = max(res, prev * (len(heights) - idx))
        
        return res
            