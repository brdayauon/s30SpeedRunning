class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.dirs = [[0,1,'u'],[0,-1,'d'],[1,0,'l'],[-1,0,'r']]
        seen = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    island = self.dfs(i,j,grid,i,j)
                    seen.add(island)
        return len(seen)
                    
    def dfs(self, i, j, grid, baseRow, baseCol):
        
        string = str(baseRow-i)+str(baseCol-j)
        stack = [(i,j)]
        
        while stack:
            i, j = stack.pop()
            grid[i][j] = 0
            
            for direction in self.dirs:
                dx = direction[0] + i
                dy = direction[1] + j
                
                if dx >= 0 and dx < len(grid) and dy >= 0 and dy < len(grid[0]) and grid[dx][dy] == 1:
                    grid[dx][dy] = 0
                    string += (str(direction[0]) + str(direction[1]) + str(dx-baseRow) + str(dy-baseCol))
                    stack.append((dx,dy))
                    
        return string