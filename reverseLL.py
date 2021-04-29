# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        dummy = fast = head
        
        while fast:
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp
            
        return prev