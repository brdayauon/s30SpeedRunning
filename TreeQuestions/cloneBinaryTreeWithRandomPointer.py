# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return root
        hm = {}
        copyRoot = NodeCopy(root.val)
        hm[root] = copyRoot
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr not in hm:
                cloneNode = NodeCopy(curr.val)
                
            currClonedNode = hm[curr]
            
            if curr.left:
                if curr.left not in hm:
                    cloneNode = NodeCopy(curr.left.val)
                    hm[curr.left] = cloneNode
                cloneNode = hm[curr.left]
                currClonedNode.left = cloneNode
                stack.append(curr.left)
            if curr.right:
                if curr.right not in hm:
                    cloneNode = NodeCopy(curr.right.val)
                    hm[curr.right] = cloneNode
                cloneNode = hm[curr.right]
                currClonedNode.right = cloneNode
                stack.append(curr.right)
            if curr.random:
                if curr.random not in hm:
                    cloneNode = NodeCopy(curr.random.val)
                    hm[curr.random] = cloneNode
                cloneNode = hm[curr.random]
                currClonedNode.random = cloneNode
                
        return hm[root]