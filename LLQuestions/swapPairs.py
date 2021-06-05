# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode()
        
        dummy.next = head
        begin = dummy
        
        #iterator to find group
        i = 0
        while head != None:
            i += 1
            #find group
            if i % 2 == 0:
                begin = self.swap(begin, head.next) #swapping in between the beginning and end
                head = begin.next #need to change head otherwise stuck in forever loop
            #move head
            else:
                head = head.next #change head
                
        return dummy.next
    
    def swap(self, begin, end):
        prev = begin
        curr = begin.next 
        first = curr
        fast = curr.next #begin.next.next
        
        while fast != end:
            curr.next = prev #change pointer
            prev = curr #update pointer
            curr = fast #update pointer
            fast = fast.next #update pointer
        
        #establish unestablish connections
        curr.next = prev #connect the left over link
        first.next = fast #connect the first node to the next node (of original list)
        begin.next = curr #basically point to the new head of the updated linked list
        
        return first