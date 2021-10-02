class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append('(')
            elif stack and c == ')':
                stack.pop()
            else:
                count += 1
        return count + len(stack)

#question was asked for Twitter