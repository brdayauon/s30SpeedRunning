"""
M- greedy/

P-
#sort               [1,10,4,11]  2:1, 7:10, 11:4, 15:11
                 V
a =  [2, 7, 11, 15]

b =  [1, 4, 10, 11]

----------------------------------------------

a =  [12,24,8,32]
b =  [13,25,32,11] b -> heap((val, index))

    L            R
a= [8,  12, 24, 32]
    L
b= [11, 13, 25, 32]                     map = original b : sortedB   
   [12, 24, 32, 8]                        13:0 25:1 32:2 11:3
                                         [24, 32, 8, 12]

res= [12, 24, 32, 8]     Intuition wise we need to find next greater number

#
heap - store nums1 in heap.. 
    each num in nums2 find. next largest number in heap
    
two pointer. 
"""
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        res = [0 for i in range(len(nums1))]
        heap = []
        for i in range(len(nums2)):
            heapq.heappush(heap, (-nums2[i], i))
        
    
        left = 0 
        right = len(nums1)-1 
        
        
        while heap:
            val, index = heapq.heappop(heap)
            val *= -1
            if nums1[right] > val:
                res[index] = nums1[right]
                right -=1
            else:
                res[index] = nums1[left]
                left += 1
        
        return res
                
            
     
            
            
            
            
            
            
            
            
            
            
            
            
            