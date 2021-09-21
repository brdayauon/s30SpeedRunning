"""
    Create a dummy Head.
    Have a pointer at l1 and at l2.
    Connect the dummy head based on the values of l1 and l2 and then move the pointers as well. 
    Then Return the LL.
    TC: O(N)
    SC: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        
        curr = dummy
        while l1 and l2:
            if l2.val <= l1.val:
                curr.next = l2
                l2 = l2.next  #curr = p2
                curr = curr.next 
            else:
                curr.next = l1 
                l1 = l1.next 
                curr = curr.next 
        if l1:
            curr.next = l1
        else:
            curr.next = l2
            
        return dummy.next

