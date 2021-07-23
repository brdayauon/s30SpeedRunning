class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { "{" : "}", "[": "]", "(":")"}
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c in mapping:
                stack.append(mapping[c])
            elif stack and c == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack)==0