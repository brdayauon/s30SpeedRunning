class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        hm = {}
        
        for i in range(len(strs)):
            word = strs[i]
            
            word = sorted(word)
            if ''.join(word) in hm:
                hm[''.join(word)].append(strs[i])
            else:
                hm[''.join(word)] = [strs[i]]
                
        for key,val in hm.items():
            res.append(val)
            
        return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        
        for i in range(len(strs)):
            temp = sorted(strs[i])
            temp = ''.join(temp)
            if temp not in hm:
                hm[temp] = [strs[i]]
            else:
                hm[temp].append(strs[i])
        res = []
        for key,val in hm.items():
            res.append(val)
        return res