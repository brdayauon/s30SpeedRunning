class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string = []
        
        for i in range(len(s)):
            c = s[i]
            if c.isalpha() or c.isdigit():
                string.append(c)

        string = ''.join(string)
        
        left = 0 
        right = len(string)-1
        
        while left < right:
            if string[left].lower() != string[right].lower():
                return False
            left += 1
            right -= 1
        return True