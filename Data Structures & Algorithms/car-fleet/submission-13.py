class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars.sort()
        cars = cars[::-1]

        res = 0
        arrival = None
        for c in cars:
            arr = (target - c[0]) / c[1]
            print(c, arr, arrival)
        
            if arrival and arr > arrival:
                res += 1

            arrival = max(arr, arrival) if arrival else arr
        
        return res + 1 if arrival else res
            

        