"""
TC: O(N)
SC: O(N)

In this problem we are given a matrix of 0s and 1s. 
We need to find out in each cell .. the nearest 0. If it's 0 its fine but 
if it is a 1 we need to find out the nearest cell that is 0.

What we do is we do a BFS.. but before that we need to find
the 1s in the matrix and mark it so we know we need to change it later. 
Then we perform bfs on each of the locations where 0 exists.

    Initialize counter for how many times..
    - Process queue:
        - do BFS for each location (check)
            Check.. is it a 0 or -1? 
            if it is -1.. mutate the array and add location to the queue 
"""
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        queue = deque([])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append(([i,j]))
                else:
                    matrix[i][j] = -1
        curr = 0
        while queue:
            size = len(queue)
            
            for i in range(size):
                x,y = queue.popleft()
                
                #look for adjacent -1s and mutate before we put in queue
                for direction in dirs:
                    dx = x + direction[0]
                    dy = y + direction[1]
                    
                    if dx >= 0 and dy >= 0 and dx < len(matrix) and dy < len(matrix[0]) and matrix[dx][dy] == -1:
                        matrix[dx][dy] = curr+1
                        queue.append((dx,dy))
            curr += 1
            
        return matrix