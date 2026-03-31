class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for b in s:
            if b == '(' or b == '{' or b == '[':
                stack.append(b)

            else:
                if not stack:
                    return False
                
                if ((b == ')' and stack[-1] == '(') 
                    or (b == '}' and stack[-1] == '{')
                    or (b == ']' and stack[-1] == '[')):
                    stack.pop()
                else:
                    return False
        
        return not stack