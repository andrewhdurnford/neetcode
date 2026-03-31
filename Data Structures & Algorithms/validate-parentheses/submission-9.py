class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = set(['(', '[', '{'])
        convert = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in o:
                stack.append(c)
            
            else:
                if not stack or stack.pop() != convert[c]:
                    return False
                
        return not stack
