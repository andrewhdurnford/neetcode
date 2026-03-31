class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0

        for i, b in enumerate(bills):
            if b == 5:
                five += 1
            elif b == 10:
                ten += 1
                five -= 1
            elif b == 20:
                twenty += 1
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3

            if min(five, ten, twenty) < 0:
                return False
        
        return True