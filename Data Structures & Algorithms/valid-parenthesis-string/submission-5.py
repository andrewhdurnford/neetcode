class Solution:
    def checkValidString(self, s: str) -> bool:
        openb = []
        star = []

        for i, c in enumerate(s):
            if c == '(':
                openb.append(i)
            elif c == '*':
                star.append(i)
            elif c == ')':
                if not openb and not star:
                    return False
                if openb:
                    openb.pop()
                else:
                    star.pop()
        
        while openb and star:
            if openb.pop() > star.pop():
                return False
    
        return not openb
