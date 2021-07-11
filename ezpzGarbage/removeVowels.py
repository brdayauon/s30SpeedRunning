class Solution:
    def removeVowels(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            c = s[i]
            if c == 'a' or c == 'e' or c == 'i' or c == 'u' or c =='o':
                continue
            else:
                res.append(c)
        return ''.join(res)