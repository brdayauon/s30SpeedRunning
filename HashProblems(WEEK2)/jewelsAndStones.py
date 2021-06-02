class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        O(1) space O(m+n) time
        """
        seen = set()
        
        for i in range(len(jewels)):
            seen.add(jewels[i])
            
        count = 0 
        for i in range(len(stones)):
            if stones[i] in seen:
                count += 1
        return count