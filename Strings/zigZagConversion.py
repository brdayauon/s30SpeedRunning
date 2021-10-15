class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = []
        
        for i in range(numRows):
            j = i
            increment = 2*(numRows-1)
            while j < len(s):
                res.append(s[j])
                if i > 0 and i < numRows-1:
                    temp = j
                    temp += ((numRows-1)*2)-2*i
                    if temp < len(s):
                        res.append(s[temp])
                j += increment
        return ''.join(res)