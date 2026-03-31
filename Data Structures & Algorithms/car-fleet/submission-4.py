class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position: return 0

        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        prevTime = None
        fleets = 0
 
        for c in range(len(cars)):
            car = cars[c]
            time = (target - car[0]) / car[1]
            if not prevTime: 
                prevTime = time
                fleets = 1
                continue

            if prevTime >= time:
                continue

            prevTime = time
            fleets += 1

        return fleets
            