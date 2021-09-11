class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        length = 0
        for i in range(len(s)):
            if s[i] != '':
                length = len(s[i])
        return length