"""
First solution: 
    TC: O(kN)
    SC: O(1)

    Create a dummy head with value of -inf incase of getting -values in linkedlist

    For each list in linked list.. we are going to merge every single one (refer to merge two sorted list problem)
    then return the dummy.next

Second solution:
    TC: O(nklogk)
    SC: O(N)

    Create a node dummy..
    Put all beginning in list into a priority queue.. 
        - learn about changing the listNode properties
                ListNode.__lt__ = (lambda a,b : a.val < b.val)

    Once everything added to heap:
        - Pop from the heap (which will be sorted when popped)
        create the LL chain to the popped item. 
    return LL
"""



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