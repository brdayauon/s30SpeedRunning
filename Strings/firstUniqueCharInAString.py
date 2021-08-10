class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}
        
        for i in range(len(s)):
            c = s[i]
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1
        
        for i in range(len(s)):
            if hm[s[i]] == 1:
                return i
        return -1