class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        res = 0
        
        self.dirs = [ [0,1], [0,-1], [1,0], [-1, 0]]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i,j, grid)
                    res += 1

        return res
    
    
    def dfs(self, i, j, grid):
        if grid[i][j] != '1':
            return 
        grid[i][j] = '#'
        for direction in self.dirs:
            row = direction[0] + i
            col = direction[1] + j
            
        
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == '1':
            #if row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == '1':
                self.dfs(row,col,grid)