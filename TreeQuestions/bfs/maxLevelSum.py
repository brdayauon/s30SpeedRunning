# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Do a level order traversal.
We find the sum.. if its greater than previous sum then we set level and check if level is greater
"""
from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        mxSum = mxLvl = float('-inf')
        while queue:
            size = len(queue)
            
            total = 0
            for i in range(size):
                curr, level = queue.popleft()
                
                total += curr.val 
                
                if curr.left:
                    queue.append((curr.left, level+1))
                if curr.right:
                    queue.append((curr.right, level+1))
            
            if total > mxSum:
                mxLvl = max(mxLvl, level)
                mxSum = max(total, mxSum)
        return mxLvl