class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for p in pair:
            if not stack:
                stack.append(p)
                continue
            
            if (target - stack[-1][0])/stack[-1][1] >= (target - p[0])/p[1]:
                continue
            else:
                stack.append(p)

        return len(stack)