class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #go to a 1 and do dfs on it
        islands = 0
        
        if not grid:
            return islands
        
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    self.dfs(grid, i, j, dirs)
                
        return islands
    
    
    def dfs(self, grid, row, col, dirs):
        if grid[row][col] != '1':
            return
        
        grid[row][col] = '#'
        
        for direction in dirs:
            x = direction[0] + row
            y = direction[1] + col
            
            #check if inbound, if valid position
            if x >= 0 and y <= len(grid[0])-1 and x <= len(grid)-1 and y >= 0 and grid[x][y] == '1':
                self.dfs(grid,x,y,dirs)
            