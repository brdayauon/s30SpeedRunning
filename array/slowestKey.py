class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        letters = { 'a': 1, 'b':2, 'c':3, 'd':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16, 'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
        currTimePressed = 0
        longestTimePressed = float('-inf')
        currLetter = None
        longestLetter = None
        for i in range(len(releaseTimes)):
            if i > 0:
                currTimePressed = releaseTimes[i]-releaseTimes[i-1]
            else:
                currTimePressed = releaseTimes[i]
            currLetter = keysPressed[i]
            if currTimePressed >= longestTimePressed:
                #same duration...check order
                if currTimePressed == longestTimePressed:
                    if letters[currLetter] > letters[longestLetter]:
                        longestLetter = currLetter
                else:
                    longestLetter = currLetter
                longestTimePressed = currTimePressed
            
        return longestLetter

