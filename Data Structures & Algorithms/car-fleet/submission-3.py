class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position: return 0
        cars = {}

        for i in range(len(position)):
            cars[position[i]] = speed[i]
        cars = collections.OrderedDict(sorted(cars.items(), reverse=True))
        stack = []
        for p, s in cars.items():
            time = (target - p) / s
            if not stack:
                stack.append(time)
                continue
            
            if stack[-1] >= time:
                continue

            stack.append(time)
        return len(stack)
            