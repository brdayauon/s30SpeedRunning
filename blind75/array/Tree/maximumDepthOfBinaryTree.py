# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #doing bfs
        
        if not root:
            return 0
        
        queue = deque([root])
        count = 0
        while queue:
            size = len(queue)
            count += 1
            
            for i in range(size):
                curr = queue.popleft()
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
        return count


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #dfs
        if not root:
            return 0
        
        stack = [(1, root)]
        mx = 0
        while stack:
            depth, curr = stack.pop()
            mx = max(mx, depth)
            if curr.left:
                stack.append((depth+1, curr.left))
            if curr.right:
                stack.append((depth+1, curr.right))
                
        return mx