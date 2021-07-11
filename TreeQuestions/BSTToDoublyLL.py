"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        dummy = Node(0)
        prev = dummy
        #level order
        stack = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
                
            root = stack.pop() 
            
            prev.right = root
            root.left = prev 
            prev = root
            
            root = root.right
        
        #because it is doubly linked list
        dummy.right.left = prev 
        prev.right = dummy.right 
        
            
        return dummy.right