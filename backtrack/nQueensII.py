class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        board = [[0 for i in range(n)] for j in range(n)]
        m = n
        def isSafe(r,c):
            for i in range(r):
                if board[i][c] == 1:
                    return False
            i = r
            j = c
            while i >= 0 and j >= 0:
                if board[i][j] == 1:
                    return False
                i -= 1
                j -= 1
            
            i = r
            j = c
            while i >= 0 and j < m:
                if board[i][j] == 1:
                    return False
                i -= 1
                j += 1
            
            return True
            #check diagonal upLeft
#             tR = r
#             for i in range(c, -1,-1):
#                 if tR < 0:
#                     break
#                 if board[tR][i] == 1:
#                     return False
#                 tR -= 1
            
#             tR = r
#             for i in range(c, len(board[0])):
#                 if tR > len(board):
#                     break
#                 if board[tR][i] == 1:
#                     return False
#                 tR += 1
            
        def backtrack(r):
            #base 
            if r == m:
                li = []
                for i in range(m):
                    tmp = []
                    for j in range(m):
                        if board[i][j] == 0:
                            tmp.append('.')
                        else:
                            tmp.append('Q')
                    li.append(''.join(tmp))
                
                res.append(li)
                return
            #logic
            for j in range(0, len(board[0])):
                if isSafe(r,j):
                    board[r][j] = 1
                    backtrack(r+1)
                    board[r][j] = 0
        
                
            
        backtrack(0)
        
        return len(res)