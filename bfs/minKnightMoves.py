class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque([(0,0)])
        steps = 0
        dirs = [[-1,-2],[-2,-1],[-1,2],[-2,1],[2,1],[1,2],[2,-1],[1,-2]]
        seen = set()
        seen.add((0,0))
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                x1,y2 = queue.popleft()
                
                if x1 == x and y == y2:
                    return steps
                
                for direction in dirs:
                    dx = x1 + direction[0]
                    dy = y2 + direction[1]
                    
                    #check boundaries too continue
                    if (dx,dy) not in seen:
                        queue.append([dx,dy])
                        seen.add((dx,dy))
            
            steps += 1
            
        return -1