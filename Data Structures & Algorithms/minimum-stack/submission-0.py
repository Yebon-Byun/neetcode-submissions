class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return min(self.min_stack)
