""" 
TC: O(N)
SC: O(N)

An iterator just focuses on the next node... 
So how do we do this? Since we are doing an in order traversal... 
We can mimic inorder traversal but in a controlled manner. 

next() 
hasNext() 
First we do dfs on the root.. 
which basically puts item into the stack and goes left all the way.
When next() is called we just pop from the stack and do dfs on the right child incase there are more nodes. 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.dfs(root)

    def next(self) -> int:
        node = self.stack.pop()
        self.dfs(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack)!= 0
    def dfs(self, root):
        while root:
            self.stack.append(root)
            root = root.left 
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()