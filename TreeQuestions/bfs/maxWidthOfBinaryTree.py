# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
- do level order traversal..
    - the max width would be the size of the queue.

"""
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        col = deque([1])
        mxWidth = float('-inf')
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                curr = queue.popleft()
                x = col.popleft()
                
                if i == 0:
                    left = x
                if curr.left:
                    queue.append(curr.left)
                    col.append(x*2)
                if curr.right:
                    queue.append(curr.right)
                    col.append((x*2)-1)
                        
            mxWidth = max(mxWidth, abs(left-x))

        return mxWidth+1