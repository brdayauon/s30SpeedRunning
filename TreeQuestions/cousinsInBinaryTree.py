""" 
TC: O(N)
SC: O(N)

Given a binary tree.. we have to figure out if given two nodes in parameter are cousins... 
One way of looking at this is checking the parents if they are not the same and if the parents are at the same level. 

Create a map that is a parents map.. where the key:value is a node:(parent, level) this way we can do our checks later on.

we can do BFS/DFS to find the two nodes we need in the tree. (probably BFS level order might be more intuitive)

    - pop from queue/stack
        - look for the nodes 
    - when we find the nodes do the check to figure out if its cousins..
        - check parents. 
            - if they are the same return False 
        - check the parent's level.
            - if they are not the same return false
        - return True

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        hm = {} #node : parent

        stack = [(root,None,-1)]
        prev = None
        count = 0
        while stack:
            curr,parent,depth = stack.pop()
            
            hm[curr] = (parent, depth)
            if curr.left:
                stack.append((curr.left, curr, depth+1))
            if curr.right:
                stack.append((curr.right, curr, depth+1))
        
        queue = deque([root])
        person1 = None
        person2 = None
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft() 
                if curr.val == x or curr.val == y:
                    if not person1:
                        person1 = curr
                    else:
                        person2 = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if person1 and person2:
                parent1 = hm[person1][0]
                parent2 = hm[person2][0]
                #parents arent same.. parent's level are same
                if (parent1.val != parent2.val) and (hm[person1][1] == hm[person2][1]):
                    return True
        return False


















# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        hm = {} #node : parent

        stack = [(root,None,-1)]
        prev = None
        count = 0
        while stack:
            curr,parent,depth = stack.pop()
            
            hm[curr] = (parent, depth)
            if curr.left:
                stack.append((curr.left, curr, depth+1))
            if curr.right:
                stack.append((curr.right, curr, depth+1))
        
        queue = deque([root])
        person1 = None
        person2 = None
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft() 
                if curr.val == x or curr.val == y:
                    if not person1:
                        person1 = curr
                    else:
                        person2 = curr
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if person1 is not None and person2 is not None:
                p1 = hm[person1][0]
                p2 = hm[person2][0]
                
                if (p1.val != p2.val) and (hm[person1][1] == hm[person2][1]):
                    return True
        return False
