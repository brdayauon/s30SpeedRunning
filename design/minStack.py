class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = Node(None)
        self.arr = []
        
    def push(self, val: int) -> None:
        newNode = Node(val)
        
        if self.root.next == None:
            self.root.next = newNode
        else:
            secondNode = self.root.next 
            self.root.next = newNode
            newNode.next = secondNode
        if len(self.arr) == 0:
            self.arr.append(val)
        elif self.arr[-1] >= val:
            self.arr.append(val)
            
    def pop(self) -> None:
        newNext = self.root.next.next
        if self.root.next:
            if self.root.next.val == self.arr[-1]:
                self.arr.pop()
            
            self.root.next = newNext

    def top(self) -> int:
        return self.root.next.val

    def getMin(self) -> int:
        return self.arr[-1]
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()