class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while (len(stack) > 0 and stack[-1][1] <= temperatures[i]):
                stack.pop()
            if len(stack) != 0:
                res[i] = stack[-1][0] - i
            stack.append([i, temperatures[i]])
        return res
            
        