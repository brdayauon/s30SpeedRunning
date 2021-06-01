# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #O(n) space
        if not head:
            return None
        
        flag = True
        
        curr = head
        odd = []
        even = []
        while curr:
            if flag:
                odd.append(curr.val)
                flag = False
            else:
                even.append(curr.val)
                flag = True
            
            curr = curr.next 
        
        dummy = ListNode()
        curr = dummy
        i = j = 0
        
        while i < len(odd):
            if i < len(odd):
                curr.next = ListNode(odd[i])
                curr = curr.next
                i += 1   
        while j < len(even):
            if j < len(even):
                curr.next = ListNode(even[j])
                curr = curr.next
                j += 1
        
        return dummy.next