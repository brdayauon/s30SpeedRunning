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