class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mnVal = float('inf')
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if val < self.mnVal:
            self.mnVal = val
        self.minStack.append(self.mnVal)
        self.stack.append(val)
        

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.minStack.pop()
        if self.minStack:
            self.mnVal = self.minStack[-1]
        else:
            self.mnVal = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mnVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()