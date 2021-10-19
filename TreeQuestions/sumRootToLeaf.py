"""
TC:
SC: 

Given a binary tree containing digits we want to find the total. How we calculate the total is from the root to the leaf.
We can do this by doing a dfs/bfs starting at the root node. 

When we pop from the stack.. what we get is the current Node and the value so far. 
To find the value so far.. we need to get the (valueSoFar*10 + the currNode.val)
We check if the node is a leaf so that we can add it to our grand total. 

To traverse.. we check if left/right nodes exist and put a tuple (left/right node, amountSoFar) into the stack.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        total = 0
        
        while stack:
            curr, amount = stack.pop()
            
            amountSoFar = amount*10+curr.val
            
            if not curr.left and not curr.right:
                total += amountSoFar
            
            if curr.left:
                stack.append((curr.left, amountSoFar))
            if curr.right:
                stack.append((curr.right, amountSoFar))
        return total