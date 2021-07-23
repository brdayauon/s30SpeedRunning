class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        #swap
        for i in range(len(matrix)):
            self.swap(matrix[i])

    def swap(self, array):
        left = 0 
        right = len(array)-1
        
        while left < right:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            
            left += 1
            right -= 1