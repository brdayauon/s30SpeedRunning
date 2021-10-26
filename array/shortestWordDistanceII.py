class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.hm = {}
        
        for i in range(len(self.wordsDict)):
            if self.wordsDict[i] not in self.hm:
                self.hm[self.wordsDict[i]] = [i]
            else:
                self.hm[self.wordsDict[i]].append(i)
    def shortest(self, word1: str, word2: str) -> int:
        
        l1 = self.hm[word1]
        l2 = self.hm[word2]
        
        mn = float('inf')
        
        for i in range(len(l1)):
            for j in range(len(l2)):
                mn = min(mn, abs(l1[i]-l2[j]))
        return mn


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)