class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        
        heap = []
        
        heapq.heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            startTime = intervals[i][0]
            endTime = intervals[i][1]
            if startTime < heap[0]:
                heapq.heappush(heap, endTime)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,endTime)
        return len(heap)
                
        