class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft = maxLeft = 0

        for i, c in enumerate(s):
            if c == '(':
                minLeft += 1
                maxLeft += 1
            elif c == ')':
                minLeft -= 1
                maxLeft -= 1
            elif c == '*':
                maxLeft += 1
                minLeft -= 1

            if maxLeft < 0: return False
            minLeft = max(minLeft, 0)
        
        return minLeft == 0
