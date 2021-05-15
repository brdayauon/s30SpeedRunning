# Time Complexity : O(n^2)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #flip image
        for i in range(len(image)):
            self.reverse(image, i, 0, len(image[0])-1)
        
        #invert image
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        
        return image
    
    def reverse(self, image, curr, left, right):
        while left <= right:
            temp = image[curr][left]
            image[curr][left] = image[curr][right]
            image[curr][right] = temp
            left += 1
            right -= 1
            
        return image