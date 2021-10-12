# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        parents = {}
        bottomLeaves = []
        #create node:parent relationship
        stack = [(root, None)]
        while stack:
            curr, parent = stack.pop()
            parents[curr] = parent
            if not curr.left and not curr.right:
                bottomLeaves.append(curr)
            if curr.left:
                stack.append((curr.left, curr))
            if curr.right:
                stack.append((curr.right, curr))
        
        
        queue = deque([])
        for i in bottomLeaves:
            queue.append(i)
            
        res = []
        while queue: 
            size = len(queue)
            level = []
            for i in range(size):
                curr = queue.popleft()
                level.append(curr.val)
                parent = parents[curr]
                
                #delete parent's child nodes
                if parent is not None:
                    if parent.left == curr:
                        parent.left = None
                    if parent.right == curr:
                        parent.right = None
                    if parent.left is None and parent.right is None:
                        queue.append(parent)
            res.append(level)
             
        return res
    
    
    
    
    
    
    
    
    
    
    
    
    