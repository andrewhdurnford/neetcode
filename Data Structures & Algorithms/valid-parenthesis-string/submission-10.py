class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == ')':
                if len(left) > 0:
                    left.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
            elif c == '*':
                star.append(i)
        
        while left and star:
            if left.pop() > star.pop():
                return False
        
        return not left
