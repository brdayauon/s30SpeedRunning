class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #swap rows and columns to get a transposed matrix
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        #then reverse each row (NlogM)
        for i in range(len(matrix)):
            self.swap(matrix, i)
            
    #swap function of a matrix
    def swap(self, matrix, row):
        left = 0
        right = len(matrix)-1
        
        while left <= right:
            temp = matrix[row][left] 
            matrix[row][left] = matrix[row][right]
            matrix[row][right] = temp
            left += 1
            right -= 1