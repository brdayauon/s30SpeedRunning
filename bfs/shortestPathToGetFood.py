class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        if not grid:
            return -1
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    queue.append([i,j])
                    break 
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        count = 0
        while queue:
            size = len(queue)
            
            for i in range(size):
                x,y = queue.popleft()
                
                if grid[x][y] == '#':
                    return count 
                #mark it
                #grid[x][y] = 'X'
                
                for direction in dirs:
                    dx = direction[0] + x
                    dy = direction[1] + y
                    
                    if dx >= 0 and dx <= len(grid)-1 and dy >= 0 and dy <= len(grid[0])-1 and grid[dx][dy] != 'X':
                        queue.append((dx,dy))
                         
                        if grid[dx][dy] == '#':
                            return count + 1
                        #mark here so it doesn't add to the queue again
                        grid[dx][dy] = 'X'
            count += 1
        return -1