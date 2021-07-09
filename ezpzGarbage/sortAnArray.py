class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #put into heap
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
        res = []
        while heap:
            num = heapq.heappop(heap)
            res.append(num)
        return res