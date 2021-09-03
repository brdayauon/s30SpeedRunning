"""
TC: O(N^26) -> O(1)?
SC: O(1) letters
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        hm = {}
        seen = set()
        
        for i in range(len(s)):
            c = s[i]
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1
        count = 0
        for key,val in hm.items():
            while val in seen:
                val -=1 
                count += 1
            if val:
                seen.add(val)
        return count