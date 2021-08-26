# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        parent = None
        left = None
        while curr:
            if curr.val < key:
                parent = curr
                curr = curr.right 
                left = False 
            elif curr.val > key:
                parent = curr 
                curr = curr.left 
                left = True
            else:
                break
        if curr:
            #has at least one or no children
            if not curr.left or not curr.right: 
                if parent:
                    if left:
                        if curr.left:
                            parent.left = curr.left 
                        elif curr.right:
                            parent.left = curr.right 
                        else:
                            parent.left = None
                    else:
                        if curr.left:
                            parent.right = curr.left 
                        elif curr.right:
                            parent.right = curr.right
                        else:
                            parent.right = None
                else:
                    if curr.left:
                        return curr.left 
                    elif curr.right:
                        return curr.right 
                    else:
                        return None
            else:
                temp = parent = curr
                curr = curr.left 
                if not curr.right:
                    parent.left = curr.left 
                else:
                    while curr.right:
                        parent = curr
                        curr = curr.right 
                    parent.right = curr.left 
                temp.val = curr.val 
        return root