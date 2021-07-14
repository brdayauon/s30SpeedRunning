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