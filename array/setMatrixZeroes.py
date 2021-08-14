class Solution(object):
    def setZeroes(self, matrix):
        firstCol = False
        firstRow = False
        
        #find if zero in the first row
        if 0 in matrix[0]:
            firstRow = True
        
        #find if zero in the first col
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstCol = True
                break
        
        #sets flags
        for row in range (len(matrix)):
            for col in range (len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
                    
        #we go on not the first row 
        for row in range(1, len(matrix)):
            #if first column is 0
            if matrix[row][0] == 0:
                for col in range(1, len(matrix[0])):
                    matrix[row][col] = 0
                    
        #now go on columns
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0
                    
        if firstRow:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
            
        if firstCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0
            
        return matrix


"""
DONE 8/13/21
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #at the end make entire top row 0
        topRowEndZero = False
        wholeTopRowZero = False
        if matrix[0][0] == 0 or matrix[0][-1] == 0:
            topRowEndZero = True
        
        #zero in top row
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                wholeTopRowZero = True
        
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                #make entire row 0
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
                    
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                #make column to 0
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        if topRowEndZero or wholeTopRowZero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        