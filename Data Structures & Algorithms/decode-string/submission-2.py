class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ''
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            
            elif c == '[':
                stack.append((cur, k))
                cur = ''
                k = 0
            
            elif c == ']':
                tmp = cur
                cur, mult = stack.pop()
                cur += tmp * mult

            else:
                cur += c
            
        return cur




                    
