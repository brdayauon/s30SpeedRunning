#BETTER VERSION
"""
better version. Need to put "in row" "in col" becz its also possible of duplicates
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #go through the board and record placement as a string into a set
        
        seen = set()
       
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                
                    
                if (str(i//3) + str(board[i][j]) + str(j//3)) in seen:
                    return False
                if (str(i)+str(board[i][j])+ "in row") in seen:
                    return False
                if (str(j)+str(board[i][j]) + "in col") in seen:
                    return False
                seen.add(str(i//3) + str(board[i][j]) + str(j//3))
                seen.add(str(i)+str(board[i][j]) + "in row")
                seen.add(str(j)+str(board[i][j]) + "in col")

        return True


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         #go through the board and record placement as a string into a set
        
#         seen = set()
#         rowSeen = set()
#         colSeen = set()
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == '.':
#                     continue
#                 if (str(i//3) + str(board[i][j]) + str(j//3)) in seen:
#                     return False
#                 if (str(i)+str(board[i][j])) in rowSeen:
#                     return False
#                 if (str(j)+str(board[i][j])) in colSeen:
#                     return False
#                 seen.add(str(i//3) + str(board[i][j]) + str(j//3))
#                 rowSeen.add(str(i)+str(board[i][j]))
#                 colSeen.add(str(j)+str(board[i][j]))

#         return True

