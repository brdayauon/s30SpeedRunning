#TC : O(kN)
#SC: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        merged = ListNode(float('-inf'))
        
        for li in lists:
            merged = self.merge(li, merged)
        return merged.next
    
    def merge(self, l1, l2):
        dummy = ListNode()
        res = dummy
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2 
                l2 = l2.next 
            
            dummy = dummy.next 
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
        return res.next 

#TC: nklogk
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        heap = []
        dummy = ListNode()
        res = dummy
        ListNode.__lt__ = (lambda a,b : a.val < b.val)
        
        for head in lists:
            if head != None:
                heapq.heappush(heap, head)
                
        while heap:
            minNode = heapq.heappop(heap)
            dummy.next = minNode
            dummy = dummy.next 
            
            if minNode.next != None:
                heapq.heappush(heap, minNode.next)
        return res.next