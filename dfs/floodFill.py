class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return []
        
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        oldColor = image[sr][sc]
        
        
        def dfs(image, row, col, newColor, oldColor,dirs):
            if image[row][col] != oldColor or image[row][col] == newColor:
                return

            image[row][col] = newColor

            for direction in dirs:
                dx = row + direction[0]
                dy = col + direction[1]

                if dx >= 0 and dx < len(image) and dy >= 0   and dy < len(image[0]) and image[dx][dy] == oldColor:
                    dfs(image, dx, dy, newColor, oldColor,dirs)
        
        
        
        dfs(image, sr, sc, newColor, oldColor,dirs)
        return image
        
    
                
