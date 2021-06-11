# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        
        #if celebrity knows that then surely that can't be the celebrity
        for i in range(1,n):
            if knows(celebrity, i):
                celebrity = i
                
        for i in range(n):
            #can't know self
            if i == celebrity:
                continue
            #if celebrity knows the person or the person does not know celebrity then there is no celebrity
            if not knows(i, celebrity) or knows(celebrity, i):
                return -1
            
        return celebrity