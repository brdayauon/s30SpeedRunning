# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        dummy = ListNode()
        dummy.next = head
        curr = head
        
        while curr:
            length += 1
            curr = curr.next 
            
        steps = (length - n)
        curr = dummy
        
        for i in range(steps):
            curr = curr.next 
            
        curr.next = curr.next.next 
        
        return dummy.next