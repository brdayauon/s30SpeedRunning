# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [([root, root.val])]
        count = 0
        while stack:
            currNode, currMxSoFar = stack.pop()
            
            if currNode.val >= currMxSoFar:
                count += 1
            
            currMxSoFar = max(currMxSoFar, currNode.val)
            
            if currNode.left:
                stack.append((currNode.left, currMxSoFar))
            if currNode.right:
                stack.append((currNode.right, currMxSoFar))
                
        return count