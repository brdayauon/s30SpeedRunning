# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #if theres nothing in the list
        if not head or k == 0:
            return head
        #what if only one thing in list
        if not head.next:
            return head
        n = head
        dummy = ListNode()
        dummy.next = head
        begin = dummy 
        
        #find length of list
        count = 0
        while n:
            n = n.next 
            count += 1
       
        n = (count-k)%count
        #if n == 0 return head because no shift
        if n == 0:
            return head
        
        curr = dummy 
        while n > 0:
            curr = curr.next 
            n -= 1
        temp = curr.next 
        newHead = temp
        #put temp.next 
        while temp.next:
            temp = temp.next 
        temp.next = begin.next 
        curr.next = None
        return newHead
        
        