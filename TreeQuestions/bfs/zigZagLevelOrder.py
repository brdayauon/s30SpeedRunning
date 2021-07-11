# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        startLeft = True
        queue = deque([root])
        res = []
        while queue:
            size = len(queue)
            currList = deque([])
            for i in range(size):
                curr = queue.popleft()
                
                if startLeft:
                    currList.append(curr.val)
                else:
                    currList.appendleft(curr.val) 
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            res.append(currList)
            if startLeft:
                startLeft = False
            else:
                startLeft = True
                   
        return res