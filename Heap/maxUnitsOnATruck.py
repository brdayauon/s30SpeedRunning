class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total = 0
        heap = []
        
        for i in range(len(boxTypes)):
            heapq.heappush(heap, (-boxTypes[i][1], boxTypes[i]))
         
        while truckSize > 0 and heap:
            units, box = heapq.heappop(heap)
            units *= -1
            box = box[0]
            box = min(box, truckSize)
            total += (units * box)
            truckSize -= box
            if truckSize == 0:
                break
             
        return total