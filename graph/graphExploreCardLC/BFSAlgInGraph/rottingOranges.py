class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Should use BFS because if DFS is used it would go through all cells
        and it is possible that a cell will be counted multiple times
        
            - Queue of coordinates.
            - Need to count freshness and populate queue if we found rotten spot
            - Use size variable because there is a differentiate situation goin on
        """
        if not grid:
            return 0
        fresh = 0 
        time = 0 
        queue = deque([])
        #perform bfs on rotten parts
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append([i,j])
        
        #if there are no fresh oranges
        if fresh == 0:
            return 0 
        
        dirs = [[0,1], [0,-1], [-1,0], [1,0]] #right, left, up, down
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                curr = queue.popleft()
                for direction in dirs:
                    row = direction[0] + curr[0]
                    col = direction[1] + curr[1]
                    
                    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 1:
                        queue.append([row,col])
                        grid[row][col] = 2
                        fresh -= 1
            time += 1
        if fresh != 0:
            return -1
        
        return time - 1

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque([])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: #fresh
                    fresh += 1
                elif grid[i][j] == 2: #rotten
                    queue.append((i,j))
        if fresh == 0:
            return 0
        minute = -1
        direction = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            size = len(queue)
            minute += 1

            for i in range(size):
                r,c = queue.popleft()

                for dirs in direction:
                    dr = dirs[0] + r
                    dc = dirs[1] + c
                    
                    if dr >= 0 and dr < len(grid) and dc >= 0 and dc < len(grid[0]) and grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        queue.append((dr,dc))
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minute