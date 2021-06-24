class Solution(object):
    def minDepth(self, root):
        
        def helper(root):
            if root.left == None and root.right == None:
                return 1
            
            if root.left == None or root.right == None:
                return 1 + helper(root.left) if root.left else 1 + helper(root.right)
            
            return 1 + min(helper(root.left), helper(root.right))
        
        if root == None:
            return 0
        
        return helper(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depthQueue = deque([1])
        queue = deque([root])
        mn = float('inf')
        while queue:
            currNode = queue.popleft()
            depth = depthQueue.popleft()
            
            if not currNode.left and not currNode.right:
                mn = min(mn, depth)
                break
            
            if currNode.left:
                queue.append(currNode.left)
                depthQueue.append(depth+1)
            if currNode.right:
                queue.append(currNode.right)
                depthQueue.append(depth+1)
            
        return mn 