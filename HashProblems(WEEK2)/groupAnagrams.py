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