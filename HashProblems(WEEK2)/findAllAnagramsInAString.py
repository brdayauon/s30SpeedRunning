class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        right = 0
        
        pHm = defaultdict()
        
        for i in range(len(p)):
            if p[i] not in pHm:
                pHm[p[i]] = 1
            else:
                pHm[p[i]] += 1
        hm = defaultdict()
        res = []
        
        while right < len(s):
            c = s[right]
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1
                    
            if left == 0 and right == 0:
                right += 1
                if hm == pHm:
                    res.append(left)
                continue
                
            if right-left < len(p): #make window big
                if hm == pHm:
                    res.append(left)
                right += 1
                
            else: #window is set
                
                hm[s[left]] -= 1
                if hm[s[left]] == 0:
                    del hm[s[left]]
                left += 1
                if hm == pHm:
                    res.append(left)
                right += 1
        
        return res