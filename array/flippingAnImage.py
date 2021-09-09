class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            self.reverse(image[i])
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
                    
        return image
    def reverse(self, image):
        left = 0
        right = len(image)-1
        
        while left < right:
            temp = image[left]
            image[left] = image[right]
            image[right] = temp
            left += 1
            right -= 1
