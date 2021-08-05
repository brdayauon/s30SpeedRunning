# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root,root.val, [root.val])]
        res = []
        while stack:
            curr, currVal, currArr = stack.pop()
                    
            if not curr.left and not curr.right and currVal == targetSum:
                res.append((currArr))
            else:
                if curr.left:
                    tempVal = curr.left.val + currVal
                    stack.append((curr.left, tempVal, currArr+[curr.left.val]))

                if curr.right:
                    tempVal = curr.right.val + currVal
                    stack.append((curr.right, tempVal, currArr+[curr.right.val]))
        
        return res