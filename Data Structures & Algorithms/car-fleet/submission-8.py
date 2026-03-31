class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        print(pair)

        for i in range(len(position)):
            
            a = (target - pair[i][0]) / pair[i][1]
            
            if not stack:
                stack.append(a)
                continue

            if a > stack[-1]:
                stack.append(a)


        return len(stack)