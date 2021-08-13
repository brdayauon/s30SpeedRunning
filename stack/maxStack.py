class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.mx = []

    def push(self, x: int) -> None:
        self.arr.append(x)
        if not self.mx:
            self.mx.append(x)
        elif self.mx[-1] > x:
            self.mx.append(self.mx[-1])
        else:
            self.mx.append(x)
            
    def pop(self) -> int:
        self.mx.pop()
        return self.arr.pop()


    def top(self) -> int:
        return self.arr[-1]

    def peekMax(self) -> int:
        return self.mx[-1]

    def popMax(self) -> int:
        mx = self.peekMax()
        curr = []
        while self.arr:
            if self.arr[-1] == mx:
                res = self.arr.pop()
                self.mx.pop()
                break
            else:
                moveTocurr = self.arr.pop()
                self.mx.pop()
                curr.append(moveTocurr)
        if not self.mx:
            mxmx = float('-inf')
        else:
            mxmx = self.mx[-1]
        while curr:
            moveToOriginal = curr.pop()
            mxmx = max(mxmx, moveToOriginal)
            self.arr.append(moveToOriginal)
            self.mx.append(mxmx)
        return res


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()