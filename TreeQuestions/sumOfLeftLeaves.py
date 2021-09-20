# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None

        queue = deque([])
        res = 0
        if not root:
            return res
        
        queue.append(root)
        count = 0

        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if isLeaf(curr.left):
                    res += curr.left.val
                    
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return res