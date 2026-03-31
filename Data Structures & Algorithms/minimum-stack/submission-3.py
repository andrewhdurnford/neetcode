class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minimum or self.minimum[-1] >= val:
            self.minimum.append(val)
        
        return None

    def pop(self) -> None:
        val = self.stack.pop()
        
        if self.minimum[-1] == val:
            self.minimum.pop()

        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        
