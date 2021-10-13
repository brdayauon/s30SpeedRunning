class Solution:
    
    def numWays(self, score):
        possibleScore = [1,2,4,6]
        self.res = []
        self.total = 0
        self.seen = set()
        self.backtrack(possibleScore, 0, [], score)
         
        return self.total, self.res
    
    def backtrack(self, possibleScore, index, path, score):
        #base case
        if score < 0:
            return
        if score == 0 and str(path) not in self.seen:
            self.res.append(list(path))
            self.seen.add(str(path))
            self.total += 1
            return
        
        for i in range(len(possibleScore)-1,-1,-1):
            #choose
            if path and possibleScore[i] == 4 and path[-1] == 4:
                continue
            path.append(possibleScore[i])
            self.backtrack(possibleScore, index, path, score - possibleScore[i])
            path.pop()
             
s = Solution()
score = 5
print(s.numWays(score))
            
                
        
        
    