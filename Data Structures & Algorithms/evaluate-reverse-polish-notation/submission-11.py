class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if not (t == '+' or t == '-' or t == '*' or t == '/'):
                stack.append(t)
            
            else:
                b = stack.pop()
                a = stack.pop()

                if t == '+':
                    res = int(a) + int(b)
                elif t == '-':
                    res = int(a) - int(b)
                elif t == '*':
                    res = int(a) * int(b)
                elif t == '/':
                    res = int(int(a) / int(b))

                print(res)
                
                stack.append(res)
        
        return int(stack[0])