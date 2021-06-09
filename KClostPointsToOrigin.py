class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        #put points into heap 
        for point in points:
          x = point[0]*point[0]
          y = point[1]*point[1]
          #put this into an array instead then heapify the array
          heapq.heappush(heap, (x+y, [point[0], point[1]]))
            
            
        res = []
        #pop elements outta heap and put into a result=[]
        for i in range(k):
          distance, coordinates = heapq.heappop(heap)
          res.append(coordinates)

        return res