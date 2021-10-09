class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        letterStack = []
        i = 0
        currStr = ""
        num = 0
        while i < len(s):
            c = s[i]
            if c.isalpha():
                currStr += c
            elif c.isdigit():
                num = (num*10) + int(c)
            elif c == '[':
                letterStack.append(currStr)
                numStack.append(num)
                num = 0
                currStr = ""
            else:
                freq = numStack.pop()
                currStr = currStr * freq
                letter = letterStack.pop()
                currStr = letter+currStr
            i += 1
        return currStr