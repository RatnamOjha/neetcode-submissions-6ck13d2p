class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if self.minstack:
            old_min = self.minstack[-1]
            new_min = min(old_min,val)
        else:
            new_min = val
        self.stack.append(val)
        self.minstack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
