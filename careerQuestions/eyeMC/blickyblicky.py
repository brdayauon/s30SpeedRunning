#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'moves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER startRow
#  3. INTEGER startCol
#  4. INTEGER endRow
#  5. INTEGER endCol
#  6. INTEGER bishopRow
#  7. INTEGER bishopCol
#
from collections import deque

def moves(n, startRow, startCol, endRow, endCol, bishopRow, bishopCol):
    def threatenCheck(dx, dy,  bishopRow, bishopCol):
        if dx-bishopRow == dy - bishopCol:
            return True
        elif -dx + bishopRow == dy - bishopCol:
            return True
        else:
            return False
    # Write your code here
    #bfs
    queue = deque([(startRow,startCol, False)])
    dirs = [[1,2], [-1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1], [-2,1]]
   
    moves = 0
    seen = set()
    seen.add((startRow, startCol))
    captured = False
    made = False
    while queue:
        size = len(queue)
       
        for i in range(size):
            moveX, moveY, captured = queue.popleft()
           
            if moveX == bishopRow and moveY  ==  bishopCol:
                captured = True
           
            for direction in dirs:
                dx = direction[0] + moveX
                dy = direction[1] + moveY
               
                if dx >= 0 and dx < n and dy >= 0 and dy < n and (dx,dy) not in seen:
                    if dx == endRow and dy == endCol:
                        return moves+1
                    if captured:
                        queue.append((dx,dy,captured))
                        seen.add((dx,dy))
                    else:
                        #check if it is not threatened
                        if dx == bishopRow and dy == bishopCol:
                            queue.append((dx,dy,captured))
                            seen.add((dx,dy))
                            continue
                        if threatenCheck(dx, dy,  bishopRow, bishopCol):
                            continue
                        else:
                            queue.append((dx,dy, captured))
                            seen.add((dx,dy))
                   
       
        moves += 1
    if made == False:
        return -1
    return moves
       
   

if __name__ == '__main__':





#!/bin/python3

import sys



class AddingStack:
    def __init__(self) -> None:
        self.arr = []
        self.increment = []
        self.cSum = 0
        pass
   
    def push(self, v : int) -> None:
        # Complete the function below
        self.cSum += v
        self.arr.append(v)
        self.increment.append(0)
        #raise Exception("push not implemented")
   
    def pop(self) -> None:
        # Complete the function below
        if not self.increment:
            return -1
        if len(self.increment) > 1:
            self.increment[-2] += self.increment[-1]
       
        #include inc
        x = self.increment.pop()
        y = self.arr.pop()
        self.cSum -= (x+y)
        return x+y
       
        #raise Exception("pop not implemented")
   
    def inc(self, i : int, v: int) -> None:
        # Complete the function below
        if self.increment:
            index = min(i, len(self.increment))-1
            self.increment[index] += v
        self.cSum += i*v
        #raise Exception("inc not implemented")
   
    def empty(self) -> bool:
        # Complete the function below
        return len(self.arr) == 0
        #raise Exception("empty not implemented")
   
    def peek(self) -> int:
        # Complete the function below
        if self.increment:
            return self.arr[-1] + self.increment[-1]
        return self.arr[-1]
        #raise Exception("peek not implemented")
   
    def sum(self) -> int:
        # Complete the function below
        return self.cSum
        #raise Exception("sum not implemented")
   

if __name__ == "__main__":