class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for p in pair:
            arrival = (target - p[0])/p[1]
            if not stack:
                stack.append(arrival)
            
            elif stack[-1] >= arrival:
                continue
            else:
                stack.append(arrival)

        return len(stack)