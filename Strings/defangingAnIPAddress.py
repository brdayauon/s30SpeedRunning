class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = []
        for i in range(len(address)):
            c = address[i]
            if c != '.':
                res.append(c)
            else:
                res.append('[.]')
        return ''.join(res)