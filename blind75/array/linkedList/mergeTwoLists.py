# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        dummy = ListNode()
        curr = dummy
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next 
            
            curr = curr.next 
            
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2
        return dummy.next