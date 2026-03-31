class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        one = 1
        two = 2
        for i in range(2, n):
            temp = two
            two = one + two
            one = temp
        
        return two