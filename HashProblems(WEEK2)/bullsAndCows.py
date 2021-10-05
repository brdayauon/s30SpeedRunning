class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = 0
        bulls = 0
        
        seenA = defaultdict(int)
        seenB = defaultdict(int)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                seenA[secret[i]] += 1
                seenB[guess[i]] += 1
        for k,v in seenB.items():
            if k in seenA:
                #need minValues of the two
                subtractBy = min(seenA[k], seenB[k])
                cows += subtractBy
        res = str(bulls)+'A'+str(cows)+'B'
        return res