class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []
        
        for stick in sticks:
            heapq.heappush(heap, stick)
        cost = 0
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            xyStick = x+y
            cost += xyStick
            heapq.heappush(heap, xyStick)
        
        return cost