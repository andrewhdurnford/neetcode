class Solution:
    def checkValidString(self, string: str) -> bool:
        l, s = [], []

        for i, c in enumerate(string):
            if c == '(':
                l.append(i)
            if c == ')':
                if len(l) > 0:
                    l.pop()
                elif len(s) > 0:
                    s.pop()
                else:
                    return False
            if c == '*':
                s.append(i)

        while l and s:
            if l.pop() > s.pop():
                return False
        
        return not l