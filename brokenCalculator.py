class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        count = 0
    
        while y >x:
            count += 1
            if y %2 == 0:
                y //= 2     
            else:
                y += 1
        
        return count + x-y