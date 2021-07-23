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


#------------------------------
#one pass
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy
        
        while n > 0:
            fast = fast.next 
            n -= 1
        fast = fast.next
        
        while fast:
            slow = slow.next 
            fast = fast.next 
        
        slow.next = slow.next.next 
        
        return dummy.next