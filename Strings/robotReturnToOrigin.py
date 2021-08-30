class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        
        direction = {'U': [0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
        
        for move in moves:
            dx = direction[move][0]
            dy = direction[move][1]
            x += dx
            y += dy
        
        if x == 0 and y == 0:
            return True
        return False