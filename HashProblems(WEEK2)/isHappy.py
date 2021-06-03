class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Need a set. We break the initial numbers and find the sum of the squares after breaking it up. Check if it's in the set (otherwise we'd get
        into a cycle) and return False if it is. Otherwise we add the total to the set and make n to be the new total. return True
        """
        seen = set()
        
        while n != 1:
            total = 0
            while n != 0:
                total += (n%10) * (n%10)
                n //= 10
                
            if total in seen:
                return False
            
            seen.add(total)
            n = total
            
        return True

        