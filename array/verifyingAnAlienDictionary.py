class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = defaultdict()
        for i in range(len(order)):
            c = order[i]
            if c not in hm:
                hm[c] = i
        def compare(word1, word2):
            p1 = 0
            p2 = 0
            #go through each of the word
            while p1 < len(word1) and p2 < len(word2):
                if word1[p1] != word2[p2]:
                    if hm[word1[p1]] > hm[word2[p2]]:
                        return False
                    else:
                        return True
                p1 += 1
                p2 += 1
            if len(word1) <= len(word2):
                return True
            
            return False
        
        #go through pairs of words
        for i in range(1, len(words)):
            if compare(words[i-1], words[i]) == False:
                return False
        return True
        
        