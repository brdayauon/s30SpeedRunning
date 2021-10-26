class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if word2 not in wordsDict or word1 not in wordsDict:
            return 0
        hm = {}
        hm[word1] = []
        hm[word2] = []
        for i in range(len(wordsDict)):
            if word1 == wordsDict[i]:
                hm[word1].append(i)
            elif word2 == wordsDict[i]:
                hm[word2].append(i)
        l1 = hm[word1]
        l2 = hm[word2]
        
        mn = float('inf')
        
        for i in range(len(l1)):
            for j in range(len(l2)):
                mn = min(mn, abs(l1[i]-l2[j]))
        return mn