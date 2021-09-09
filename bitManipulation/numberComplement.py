class Solution:
    def findComplement(self, num: int) -> int:
        bs = bin(num)
        bs = list(bs)
        for i in range(2,len(bs)):
            if bs[i] == '0':
                bs[i] = '1'
            else:
                bs[i] = '0'
        
        return int(''.join(bs),2)