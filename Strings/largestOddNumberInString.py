class Solution:
    def largestOddNumber(self, num: str) -> str:
        left = 0
        right = len(num)-1
        
        while left < right:
            if int(num[right]) % 2 != 0:
                return num[left:right+1]
            else:
                right -= 1
                
        if left == right and int(num[left]) % 2 != 0:
            return num[left]
            
                
        return ""