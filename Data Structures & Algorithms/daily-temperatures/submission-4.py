class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []

        for i, t in enumerate(temps):
            while stack and stack[-1][0] < t:
                idx = stack.pop()[1]
                res[idx] = i - idx
            
            stack.append([t, i])
        
        return res