# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #reverse LL
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        #add LL
        p1 = l1 
        p2 = l2
        dummy = ListNode()
        x = y = 0
        carry = 0
        curr = dummy
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
            carry = total // 10
            
            curr.next = ListNode(total % 10)
            curr = curr.next
            if p1:
                p1 = p1.next 
            if p2:
                p2 = p2.next 
        if carry > 0:
            curr.next = ListNode(1)        
        #reverse again
        return self.reverse(dummy.next)
        
    def reverse(self, head):
        if not head:
            return head
        prev = None
        curr = temp = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev