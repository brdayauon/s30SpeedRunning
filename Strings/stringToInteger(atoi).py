class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        res = deque([])
        #white space
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
            
        #get sign
        isPositive = True
        while i < len(s) and (s[i] == '+' or s[i] == '-'): #can convert to if statement
            if s[i] == '-':
                isPositive = False
                i += 1
                break
            elif s[i] == '+':
                i+= 1
                break
            i += 1
            
        res = [] #only append digits
        while i < len(s) and s[i].isdigit():
            res.append(s[i])
            i += 1
        
        res = self.convertToInt(res, isPositive) #convert to number
        if res < -2147483648: #check if it is lower than the minInt and maxInt
            return -2147483648
        elif res > 2147483647:
            return 2147483647
        return res
    def convertToInt(self, string, isPositive):
        res = 0
        i = 0
        while i < len(string):
            if string[i].isnumeric():
                res *= 10
                res += int(string[i])
            i += 1
        if not isPositive:
            res *= -1
        return res
    