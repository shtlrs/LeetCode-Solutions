class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.minstack:
            self.minstack.append(val)
        else:
            if val < self.minstack[-1]:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            last = self.stack.pop()
            self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
 
    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()