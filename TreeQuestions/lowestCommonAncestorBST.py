# Time Complexity : O(N)
# Space Complexity : O(H) h = height of the tree
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no


# Your code here along with comments explaining your approach


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Can take advantage of the Binary Search Tree property to find LCA.
        if both nodes a smaller go left.. else go right. 
        return root otherwise
        """
        if not root:
            return None
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p, q)
        else:
            return root

    def lowestCommonAncestorIterative(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        "iterative solution"

        if not root:
            return None 
        stack=[root]

        while stack:
            curr = stack.pop()

            if p.val < curr.val and q.val < curr.val:
                stack.append(curr.left)
            elif p.val > curr.val and q.val > curr.val:
                stack.append(curr.right)
            else:
                return curr
        return -1 

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.right = TreeNode(8)
root.right.left = TreeNode(6)

s = Solution()
res = s.lowestCommonAncestorIterative(root, root.right.left, root.right.right)
print(res.val)