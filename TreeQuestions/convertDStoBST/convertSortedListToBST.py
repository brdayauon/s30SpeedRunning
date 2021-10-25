# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findMid(head):
            slow = fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next 
                fast = fast.next.next
            #important case... when slowPtr == head
            if prev:
                prev.next  = None
            return slow
                
        def helper(head):
            if not head:
                return None
            
            midNode = findMid(head) 
        
            root = TreeNode(midNode.val)
            
            if head == midNode:
                return root
            
            root.left = helper(head)
            root.right = helper(midNode.next)
        
            return root
        
        return helper(head)