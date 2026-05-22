class Solution:
    def checkValidString(self, string: str) -> bool:
        l, s = [], []

        for i, c in enumerate(string):
            if c == '(':
                l.append(i)
            elif c == ')':
                if l:
                    l.pop()
                elif s:
                    s.pop()
                else:
                    return False
            elif c == '*':
                s.append(i)
            else:
                return False
        
        while l and s:
            if l.pop() > s.pop(): return False
        
        return not l