# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hm = {}
        
        stack = [root]
        
        while stack:
            curr = stack.pop()
            
            if curr.val not in hm:
                hm[curr.val] = 1
            else:
                hm[curr.val] += 1
                
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        mx = float('-inf')
        res = set()
    
        for k,v in hm.items():
            if mx == v:
                res.add(k)
            elif mx < v:
                res = set()
                res.add(k)
                mx = v
        return res

#10.24 solution O(N) time complexity O(1) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def inOrderFindMaxOccurrences(root):
            stack = []
            mxCount = 0
            prevNode = None
            currCount = 0
            
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left 
                root = stack.pop()

                if prevNode == None:
                    prevNode = root.val 
                    currCount = 1
                else:
                    if root.val != prevNode:
                        currCount = 1
                    else:
                        currCount += 1
                prevNode = root.val 
                mxCount = max(mxCount, currCount)
                root = root.right 
        
            return mxCount
        
        maxOccurrence = inOrderFindMaxOccurrences(root)
        stack = []
        prevNode = None
        currCount = 0
        res = set()
        while stack or root:
            while root:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            
            if prevNode == None:
                prevNode = root.val 
                currCount = 1
            else:
                if root.val != prevNode:
                    currCount = 1
                else:
                    currCount += 1
             
            prevNode = root.val
            if currCount == maxOccurrence:
                res.add(root.val)
            
            root = root.right
            
        return res
                
                
                
                
                
                
                
                
                
        