class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hm = {} #{number : frequency}
        #get frequency
        for i in range(len(nums)):        
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]] += 1
        #put items in heap 
        for key,values in hm.items():
            heapq.heappush(heap, (-values, key))
        res = []
        #pop items from heap
        while k > 0:
            values, key = heapq.heappop(heap)
            res.append(key)
            k -= 1
            
        return res