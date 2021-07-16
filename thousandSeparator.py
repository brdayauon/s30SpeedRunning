class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return '0'
        res = deque([])
        steps = 0
        while n != 0:
            
            number = n % 10
            if steps % 3 == 0:
                res.appendleft('.')
            res.appendleft(str(number))
            
            n //= 10
            steps += 1
        
        if res and res[-1] == '.':
            res.pop()
            
        return ''.join(res)