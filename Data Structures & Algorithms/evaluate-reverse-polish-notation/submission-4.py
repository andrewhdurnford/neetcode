class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                stack.append(int(token))
            else:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    stack.append(-stack.pop() + stack.pop())
                elif token == "*":
                    stack.append(int(stack.pop() * stack.pop()))
                elif token == "/":
                    divisor = stack.pop()
                    stack.append(int(stack.pop() / divisor))
        return stack[0]