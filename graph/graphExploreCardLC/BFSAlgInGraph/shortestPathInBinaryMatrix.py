# check if starting is 1 and if the current r/c is at destination
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1 
        
        queue = deque([(0,0)])
        count = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
        grid[0][0] = 1
        while queue:
            size = len(queue)
            count += 1
            for i in range(size):
                r,c = queue.popleft()
                
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return count
                 
                for direction in directions:
                    dr = direction[0] + r
                    dc = direction[1] + c
                    
                    #check bounds 
                    if dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid[0]) and grid[dr][dc] == 0:
                        if dr == len(grid)-1 and dc == len(grid[0])-1:
                            return count + 1
                        
                        queue.append((dr,dc))
                        grid[dr][dc] = 1
                        
                        
        return -1
                