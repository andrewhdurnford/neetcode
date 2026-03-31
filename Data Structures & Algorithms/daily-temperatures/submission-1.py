class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            if not stack:
                stack.append(i)
                continue
            
            if t <= temps[stack[-1]]:
                stack.append(i)
                continue
            
            while stack and t > temps[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)
            

        return res
                

            
