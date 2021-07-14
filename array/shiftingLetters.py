class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix = 0
        for i in range(len(shifts)-1,-1,-1):
            shifts[i] = shifts[i]+prefix
            prefix = shifts[i]
            
        res = []
        letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        s = list(s)
        for i in range(len(s)):
            c = s[i]
            for j in range(len(letters)):
                if c == letters[j]:
                    newShift = (j + shifts[i]) % 26
            
            s[i] = letters[newShift]
        
        return ''.join(s)