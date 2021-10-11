"""
Go to each cell..if it is a one increase total. If there's a diagonal one.. check up and left to see if it valid square
then increase total if valid
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        total = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    total += 1
                    #check second square,thirdsquare blahblah
                    #while diagonal is a 1
                    #flag to break outta there
                    tempI = i+1
                    tempJ = j+1
                    flag = 1
                    while (tempI < len(matrix)) and (tempJ < len(matrix[0])) and (flag == 1): #took out (matrix[tempI+1][tempJ+1] == 1) 
                        if matrix[tempI][tempJ] != 1:
                            break
                        flag = 1
                        #go up
                        for k in range(tempI-1,i-1,-1):
                            if matrix[k][tempJ] != 1:
                                flag = -1
                                break
                        if flag == -1:
                            break
                        #go left
                        for k in range(tempJ-1,j-1,-1):
                            if matrix[tempI][k] != 1:
                                flag = -1
                                break
                        if flag == -1:
                            break
                        tempI += 1
                        tempJ += 1
                        total += 1
                        
        return total
    