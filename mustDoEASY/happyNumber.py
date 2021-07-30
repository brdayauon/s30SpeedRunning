class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        seen = set()
        seen.add(n)
        while n != 1:
            total = 0
            while n != 0:
                square = (n%10)*(n%10)
                total += (square)
                n //= 10
            if total in seen:
                return False
            seen.add(total)
            n = total
            
        if total == 1:
            return True
        
        return False
        