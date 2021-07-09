class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        queue = deque([])
        #look for rotten orange if none then return -1
        noRotten = True
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    noRotten = False
                    queue.append(([i,j]))
                if grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
     
        minutes = 0
        while queue:
            size = len(queue)
            for i in range(size):
                row,col = queue.popleft()
                
                #mark
                #check four direct adjacent
                if col+1 < len(grid[row]) and grid[row][col+1] == 1:
                    queue.append([row,col+1])
                    fresh -= 1
                    grid[row][col+1] = 2
                if col-1 >= 0 and grid[row][col-1] == 1:
                    queue.append([row,col-1])
                    fresh -= 1
                    grid[row][col-1] = 2
                if row+1 < len(grid) and grid[row+1][col] == 1:
                    queue.append([row+1,col])
                    fresh -= 1
                    grid[row+1][col] = 2
                if row-1 >= 0 and grid[row-1][col] == 1:
                    queue.append([row-1,col])
                    fresh -= 1
                    grid[row-1][col] = 2
                    
            minutes += 1
            
        if fresh != 0:
            return -1
        #check for fresh
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             return -1
        
        
        return minutes-1