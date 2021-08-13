class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.mn = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.mn:
             self.mn.append(val)
        else:
            mn = self.mn[-1]
            if val < mn:
                self.mn.append(val)
            else:
                self.mn.append(mn)

    def pop(self) -> None:
        self.arr.pop()
        self.mn.pop()
        

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mn[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()