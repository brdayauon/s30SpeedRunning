class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        
        #first column
        for j in range(1, len(obstacleGrid)):
            if obstacleGrid[j][0] == 0 and obstacleGrid[j-1][0] == 1:
                obstacleGrid[j][0] = 1
            else:
                obstacleGrid[j][0] = 0
        
        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0 and obstacleGrid[0][i-1] == 1:
                obstacleGrid[0][i] = 1
            else:
                obstacleGrid[0][i] = 0
        
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] += obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]