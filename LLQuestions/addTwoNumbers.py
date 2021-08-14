# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        p1 = l1
        p2 = l2
        carry = 0
        
        x = y = total = 0
        while p1 or p2:
            if p1:
                x = p1.val 
            else:
                x = 0
            if p2:
                y = p2.val 
            else:
                y = 0
                
            total = x + y + carry
            
            # // not %
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            if p1:
                p1 = p1.next 
            if p2:
                p2 = p2.next 
        if carry > 0:
            curr.next = ListNode(1)
        return dummy.next


""" 
DONE 8/13/21
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        x=y=0
        c = 0
        total = 0
        while l1 or l2:
            if l1:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2:
                y = l2.val 
                l2 = l2.next 
            else:
                y = 0
            total = x+y+c
            
            dummy.next = ListNode(total%10)
            c = total//10
            dummy = dummy.next 
        if c != 0:
            dummy.next = ListNode(1)
        return temp.next
                