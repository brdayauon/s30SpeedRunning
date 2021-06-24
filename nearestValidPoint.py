class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = mnDist = float('inf')
        
        for i in range(len(points)):
            manHattanDist = 0
            
            x2 = points[i][0]
            y2 = points[i][1]
            
            #check validity
            if x2 == x or y2 == y:
                manHattanDist = abs(x2 - x) + abs(y2 - y)
                
                if manHattanDist < mnDist:
                    res = i
                    mnDist = manHattanDist
        if res == float('inf'):
            return -1
        return res


"""
NOT OPTIMAL AT THE BOTTOM
"""
        
        
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        hm ={} #distance : index
        mn = float('inf')
        #mx = float('-inf')
        
        for i in range(len(points)):
            manHattanDist = 0
            #for j in range(len(points[0])):
            x2 = points[i][0]
            y2 = points[i][1]
            
            #check validity
            if x2 == x or y2 == y:
                manHattanDist = abs(x2 - x) + abs(y2 - y)
                mn = min(mn, manHattanDist)
                #mx = max(mx, manHattanDist)
                if manHattanDist not in hm:
                    hm[manHattanDist] = []
                hm[manHattanDist].append(i)
                
        if len(hm) == 0:
            return -1
        
        lst = hm[mn]
        return lst[0]
    
#         for i in range(mn,mx):
#             lst = hm[mn]
#             return lst[0]
        
        
        