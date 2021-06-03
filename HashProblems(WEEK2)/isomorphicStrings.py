class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        need two Maps. Iterate over each string. 
        When we go over the first string, map each character to the character in the other string. 
        If it's not the same return false. Do the same for the other string.
        return True
        """
        sMap = {}
        tMap = {}
        
        for i in range(len(s)):
            c = s[i]
            if c not in sMap:
                sMap[c] = t[i]
            else:
                if sMap[c] != t[i]:
                    return False
                
        for i in range(len(t)):
            c = t[i]
            if c not in tMap:
                tMap[c] = s[i]
            else:
                if tMap[c] != s[i]:
                    return False
        return True