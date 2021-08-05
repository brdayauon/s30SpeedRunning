# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        queue = deque([(root,root.val)])
        
        while queue:
            curr, currVal = queue.popleft()
            if not curr.right and not curr.left:
                if currVal == targetSum:
                    return True
            if curr.right:
                tempVal = curr.right.val 
                queue.append((curr.right, tempVal + currVal))

            if curr.left:
                tempVal = curr.left.val 
                queue.append((curr.left, tempVal + currVal))
            
        return  False