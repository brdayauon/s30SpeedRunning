class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        
        for i in range(len(s)):
            c = s[i]
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1
        hm2 = {}    
        for i in range(len(t)):
            c = t[i]
            if c not in hm2:
                hm2[c] = 1
            else:
                hm2[c] += 1
        
        return hm == hm2