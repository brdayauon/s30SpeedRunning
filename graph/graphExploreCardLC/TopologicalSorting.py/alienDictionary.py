class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #build adj list
        hm = self.buildAdjList(words)
        indegree = [0 for i in range(26)]
        letterToIndex = {'a': 0, 'b':1, 'c':2, 'd':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        indexToLetter = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
        print(hm)
        for letter,neighbors in hm.items():
            for incoming in neighbors:
                index = letterToIndex[incoming]
                indegree[index] += 1
        stack = []
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0 and indexToLetter[i] in hm:
                stack.append(indexToLetter[i])
                res.append(indexToLetter[i])
                
        while stack:
            curr = stack.pop()
            
            if curr in hm:
                neighbors = hm[curr]
                for n in neighbors:
                    nIndex = letterToIndex[n]
                    indegree[nIndex] -= 1
                    if indegree[nIndex] == 0:
                        stack.append(n)
                        res.append(n)
        for i in range(len(indegree)):
            if indegree[i] != 0:
                return ""
       
        return ''.join(res)
                    
    
    def buildAdjList(self, words):
        hm = defaultdict(set)
        for word in words:      #IMPORTANT
            for c in range(len(word)):
                if word[c] not in hm:
                    hm[word[c]] = set()
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            if word1.startswith(word2) and len(word1) > len(word2): #IMPORTANT
                return {} #clear the map
            p1 = 0
            p2 = 0
            while p1 < len(word1) and p2 < len(word2):
                if word1[p1] != word2[p2]:
                    hm[word1[p1]].add(word2[p2])
                    break
                p1 += 1
                p2 += 1
        return hm