class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificQueue = deque()
        atlanticQueue = deque()
        for i in range(len(heights)):
            pacificQueue.append((i, 0))
            atlanticQueue.append((i, len(heights[0]) - 1))
        for i in range(len(heights[0])):
            pacificQueue.append((0, i))
            atlanticQueue.append((len(heights) - 1, i))
        
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        seen = set()
        while pacificQueue:
            size = len(pacificQueue)
            for i in range(size):
                r,c = pacificQueue.popleft()
                seen.add((r,c))
                for direction in dirs:
                    dx = direction[0] + r
                    dy = direction[1] + c
                    
                    if dx >= 0 and dx < len(heights) and dy < len(heights[0]) and dy >= 0 and heights[dx][dy] >= heights[r][c] and (dx,dy) not in seen:
                        #mark it 
                        seen.add((dx,dy))
                        pacificQueue.append((dx,dy))
        
        atlanticSeen = set()
        while atlanticQueue:
            size = len(atlanticQueue)
            for i in range(size):
                r,c = atlanticQueue.popleft()
                atlanticSeen.add((r,c))
                for direction in dirs:
                    dx = direction[0] + r
                    dy = direction[1] + c
                    if dx >= 0 and dx < len(heights) and dy < len(heights[0]) and  dy >= 0 and heights[dx][dy] >= heights[r][c] and (dx,dy) not in atlanticSeen:
                            atlanticSeen.add((dx,dy))
                            atlanticQueue.append((dx,dy))
        res = []
        for i in atlanticSeen:
            if i in seen:
                res.append(list(i))
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        