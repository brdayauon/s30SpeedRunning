class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        heap = []
        
        for i in range(len(intervals)):
            heapq.heappush(heap, (intervals[i][0],intervals[i]))
        prevEnd = None
        while heap:
            start, interval = heapq.heappop(heap)
            
            if prevEnd == None:
                prevEnd = interval[1]
                continue
            if prevEnd > start:
                return False
            prevEnd = interval[1]
            
        return True